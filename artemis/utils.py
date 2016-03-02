"""
Lots of helper functions to ease tests
"""
from collections import deque
import os
import itertools
import requests
import logging
from flask import json
import werkzeug
from artemis.configuration_manager import config
import subprocess
import select
import flask_restful
from copy import deepcopy
import re
import jsonpath_rw as jp
import functools

_api_main_root_point = 'http://localhost/'

_api_current_root_point = _api_main_root_point + config['API_POINT_PREFIX'] + 'v1/'


def instance_data_path(dataset):
    p = config['DATASET_PATH_LAYOUT']
    return p.format(dataset=dataset)


def nav_path(dataset):
    p = config['NAV_FILE_PATH_LAYOUT']
    return p.format(dataset=dataset)


def new_fusio_files_path(dataset):
    p = config['NEW_FUSIO_FILE_PATH_LAYOUT']
    return p.format(dataset=dataset.upper())


def api(url):
    """
    default call to the api
    call http://endpoint/v1/{url}

    return the response and the url called (it might have been modified with the normalization)
    """
    norm_url = werkzeug.url_fix(_api_current_root_point + url)  # normalize url

    raw_response = requests.get(norm_url)

    response = json.loads(raw_response.text)

    # we don't want full urls in the response, since it will change depending on where the test in run
    # so we remove the server address
    pattern = "http:\\\\/\\\\/.+?\\\\/v1\\\\/"
    for path in jp.parse('$..href').find(response):
        key = None
        if isinstance(path.path, jp.Fields):
            # case where the container is a dict
            key = str(path.path)
        elif isinstance(path.path, jp.jsonpath.Index):
            # case where the container is a list
            key = path.path.index
        path.context.value[key] = re.sub(pattern, "http:\\/\\/SERVER_ADDR\\/v1\\/", path.value)

    return response, norm_url


def get_ref(call_id):
    """
    get the associated reference for this API call

    the reference is stored in the REFERENCE_FILE_PATH directory with the same name as the call_id

    TODO: I think it might be nice to access the ref from another platform
    It would thus be possible to execute the tests on a dev computer and access the ref
    on the CI platform
    """
    assert os.path.exists(config['REFERENCE_FILE_PATH']), \
        "no reference directory found: {} does not exists".format(config['REFERENCE_FILE_PATH'])

    ref_filename = os.path.join(config['REFERENCE_FILE_PATH'], call_id)

    assert os.path.isfile(ref_filename), \
        "No reference available for query {}, we can't test anything".format(call_id)

    _file = open(ref_filename, 'r')

    dict_response = json.load(_file)

    return dict_response


def get_ref_full_response(call_id):
    all_ref_dict = get_ref(call_id)

    return all_ref_dict['full_response']


def compare_with_ref(resp, call_id, checker):
    """
    compare the answer to it's reference.

    if a mask is provided we only compare the filtered field
    """
    ref_full_response = get_ref_full_response(call_id)

    #we filter again the reference with the mask to have less
    # differences when the output or the mask change
    ref = checker.filter(ref_full_response)

    checker.compare(resp, ref)


def launch_exec_background(exec_name, args):
    logging.getLogger(__name__).debug('Launching ' + exec_name + ' ' + ' '.join(args))
    args.insert(0, exec_name)
    proc = subprocess.Popen(args)

    return proc


def filter_dict(response, mask):
    """
    filter a dict using the marshal of flask restful
    """
    if not mask:
        return response  # without mask we do not filter
    return flask_restful.marshal(response, mask)


class WhiteListMask(object):
    def __init__(self, mask):
        self.mask = mask

    def filter(self, response):
        return filter_dict(response, self.mask)


class BlackListMask(object):
    """
    >>> bobette = {'tutu': 1,
    ... 'tata': [1, 2],
    ... 'toto': {'bob':12, 'bobette': 13, 'nested_bob': {'bob': 3}},
    ... 'tete': ('tuple1', ['ltuple1', 'ltuple2']),
    ... 'titi': [{'a':1}, {'b':1}]}
    >>> bl = BlackListMask(['$..bob'])
    >>> print bl.filter(bobette)
    {'tata': [1, 2], 'toto': {'bobette': 13, 'bob': None, 'nested_bob': {'bob': None}}, 'tutu': 1, 'tete': ('tuple1', ['ltuple1', 'ltuple2']), 'titi': [{'a': 1}, {'b': 1}]}
    """
    def __init__(self, masks=[]):
        self.masks = masks

    def _black_list_filter(self, dct):
        for mask in self.masks:
            paths_found = jp.parse(mask).find(dct)
            for path in paths_found:
                # context.value is a reference to the object to which path belongs
                # Ex:
                # {"a": {"b": {"c":42} } }
                # the given jsonpath is $..c
                # the path to c will be "c" and its context.value is {"c": 42}
                # the path to {"c": 42} is "b" and its context.value is {"b": {"c": 42}}
                # etc...
                if isinstance(path.path, jp.Fields):
                    # case where the container is a dict
                    path.context.value[str(path.path)] = None
                elif isinstance(path.path, jp.jsonpath.Index):
                    # case where the container is a list
                    path.context.value[path.path.index] = None

    def filter(self, response):
        return self._black_list_filter(response)


def comparator(compare_generator):
    def compare(obj1, obj2):
        """
        To decide that 2 objects are equals, we loop through all values of the
        compare_generator and stop at the first non equals value

        Note: the fillvalue is the value used when a generator is consumed
        (if the 2 generators does not return the same number of elt).
        by setting it to object(), we ensure that it will be !=
        from any values returned by the other generator
        """
        for a, b in itertools.izip_longest(compare_generator(obj1),
                                           compare_generator(obj2),
                                           fillvalue=object()):
            if a != b:
                return -1 if a < b else 1
        return 0
    return compare


def sort_all_list_dict(response):
    """
    depth first search on a dict.
    sort all list in the dict
    """
    queue = deque()

    def magic_sort(elt):
        to_check = ['uri', 'id', 'label', 'name', 'href']
        for field in to_check:
            if field in elt:
                yield elt[field]
        yield elt

    def add_elt(elt, first=False):
        if isinstance(elt, (list, tuple)):
            if isinstance(elt, list):
                elt.sort(cmp=comparator(magic_sort))
            for val in elt:
                queue.append(val)
        elif hasattr(elt, 'iteritems'):
            for k, v in elt.iteritems():
                queue.append((k, v))
        elif first:  # for the first elt, we add it even if it is no collection
            queue.append(elt)

    add_elt(response, first=True)
    while queue:
        elem = queue.pop()
        add_elt(elem)


class RetrocompatibilityMask(object):
    def __init__(self):
        pass

    def filter(self, response):
        """For retrocompatibility we don't care about sorting, so we sort all lists"""
        r = deepcopy(response)

        sort_all_list_dict(r)
        return r


def check_equals(a, b):
    """
    TODO!

    check the equality without stoping the test on error (the test will still be in error if that's the case)
    equivalent to BOOST_CHECK_EQUALS


    For the moment it is a simple assert, but try to use this shell as often as possible.

    the implementation might be done with hidden variables and a default decorator on each test function
    """
    assert a == b


def is_subset(obj1, obj2):
    """
    Check that dict1 is a subset of dict2, so that each element of dict 1 is contained in dict2

    >>> bobette = {'tutu': 1,
    ... 'tata': [1, 2],
    ... 'toto': {'bob':12, 'bobette': 13, 'nested_bob': {'bob': 3}},
    ... 'tete': ('tuple1', ['ltuple1', 'ltuple2']),
    ... 'titi': [{'a':1}, {'b':1}]}

    >>> from copy import deepcopy
    >>> bob = deepcopy(bobette)
    >>> del bob['tete']

    >>> is_subset(bob, bobette)

    >>> is_subset(bobette, bob)
    Traceback (most recent call last):
        ...
    AssertionError: assert 'tete' in {'tata': [1, 2], 'titi': [{'a': 1}, {'b': 1}], 'toto': {'bob': 12, 'bobette': 13, 'nested_bob': {'bob': 3}}, 'tutu': 1}

    >>> is_subset({}, bob) # empty dict is a subset of all dict

    >>> modified_bobette = deepcopy(bobette)
    >>> modified_bobette['toto']['nested_bob']['bob'] = 'changed'

    >>> is_subset(modified_bobette, modified_bobette)

    >>> is_subset(bobette, modified_bobette)
    Traceback (most recent call last):
        ...
    AssertionError: assert 3 == 'changed'

    >>> is_subset(modified_bobette, bobette)
    Traceback (most recent call last):
        ...
    AssertionError: assert 'changed' == 3

    >>> multibob = {'multibob': [deepcopy(bob), deepcopy(bob)]}

    >>> is_subset(multibob, multibob)

    >>> modified_multibob = deepcopy(multibob)
    >>> del modified_multibob['multibob'][1]['titi']

    >>> is_subset(modified_multibob, multibob)

    >>> is_subset(multibob, modified_multibob)
    Traceback (most recent call last):
        ...
    AssertionError: assert 'titi' in {'tata': [1, 2], 'toto': {'bob': 12, 'bobette': 13, 'nested_bob': {'bob': 3}}, 'tutu': 1}
    """
    if type(obj1) not in (dict, list) or type(obj2) != type(obj1):
        assert obj1 == obj2
        return

    for k, v in obj1.iteritems():
        assert k in obj2

        v2 = obj2[k]
        if type(v) is dict:
            is_subset(v, v2)
        elif type(v) is list:
            assert type(v2) is list
            for s1, s2 in zip(v, v2):
                is_subset(s1, s2)
        else:
            assert v == v2


class PerfectComparator(object):
    """
    Classic comparator, all dict must be perfectly equals
    """
    @staticmethod
    def compare(response, ref):
        return check_equals(response, ref)


class SubsetComparator(object):
    """
    All element in the reference must be in the new response

    It tests that the api is always retro compatible (there can be more stuff, but never less)
    """
    @staticmethod
    def compare(response, ref):
        return is_subset(ref, response)


def compose_functions(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


class Checker(object):
    """
    Navitia Response checker

    provides 2 methods:
    - one to filter the navitia response
    - one to compare the filtered response
    """
    def __init__(self, filters, comparator=PerfectComparator()):
        self._filters = filters
        self._comparator = comparator

    def filter(self, *args, **kwargs):
        # we want that each filter in self._filters do its filter
        # It turns out that we want a function composition
        fs = [f.filter for f in self._filters]
        return compose_functions(*fs)(*args, **kwargs)

    def compare(self, *args, **kwargs):
        return self._comparator.compare(*args, **kwargs)


def launch_exec(cmd, additional_args=[], additional_env=None):
    """
    Launch an exec with args, log the outputs
    return a tuple with (return code, process)
    the process can be used for example to kill the process later
    """
    logger = logging.getLogger(__name__)
    logger.debug('Launching ' + cmd + ' '.join(additional_args))

    fdr, fdw = os.pipe()
    new_env = os.environ.copy()
    if additional_env:
        for k, v in additional_env.iteritems():
            new_env[k] = v
    try:
        splited = cmd.split(' ')
        splited.extend(additional_args)
        proc = subprocess.Popen(splited, stderr=fdw,
                         stdout=fdw, close_fds=True, env=new_env)
        poller = select.poll()
        poller.register(fdr)
        while True:
            if poller.poll(1000):
                line = os.read(fdr, 1000)
                logger.debug(line)
            if proc.poll() is not None:
                break

    finally:
        os.close(fdr)
        os.close(fdw)

    return proc.returncode, proc
