"""
Lots of helper functions to ease tests
"""
import os
import requests
import logging
from flask import json
import werkzeug
from artemis.configuration_manager import config
import subprocess
import select
import flask_restful

_api_main_root_point = 'http://localhost/'

_api_current_root_point = _api_main_root_point + config['API_POINT_PREFIX'] + 'v1/'


def api(url):
    """
    default call to the api
    call http://endpoint/v1/{url}

    return the response and the url called (it might have been modified with the normalization)
    """
    norm_url = werkzeug.url_fix(_api_current_root_point + url)  # normalize url

    raw_response = requests.get(norm_url)

    response = raw_response.json()

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
    def __init__(self, mask):
        self.mask = mask

    def filter(self, response):
        raise "TODO"


def check_equals(a, b):
    """
    TODO!

    check the equality without stoping the test on error (the test will still be in error if that's the case)
    equivalent to BOOST_CHECK_EQUALS


    For the moment it is a simple assert, but try to use this shell as often as possible.

    the implementation might be done with hidden variables and a default decorator on each test function
    """
    assert a == b


def is_subset(dict1, dict2):
    """
    Check that dict1 is a subset of dict2, so that each element of dict 1 is contained in dict2

    >>> bob = {'tutu': 1,
    ... 'tata': [1, 2],
    ... 'titi': [{'a':1}, {'b':1}]}

    >>> bobette = {'tutu': 1,
    ... 'tata': [1, 2],
    ... 'toto': {'bob':12, 'bobette': 13, 'nested_bob': {'bob': 3}},
    ... 'tete': ('tuple1', ['ltuple1', 'ltuple2']),
    ... 'titi': [{'a':1}, {'b':1}]}

    >>> is_subset(bob, bobette)

    >>> is_subset(bobette, bob)
    Traceback (most recent call last):
      File "/usr/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest artemis.utils.is_subset[3]>", line 1, in <module>
        is_subset(bobette, bob)
      File "/home/antoine/dev/artemis/artemis/utils.py", line 159, in is_subset
        assert k in dict2
    AssertionError: assert 'toto' in {'tata': [1, 2], 'titi': [{'a': 1}, {'b': 1}], 'tutu': 1}

    >>> is_subset({}, bob) # empty dict is a subset of all dict

    >>> from copy import deepcopy
    >>> modified_bobette = deepcopy(bobette)
    >>> modified_bobette['toto']['nested_bob']['bob'] = 'changed'

    >>> is_subset(modified_bobette, modified_bobette)

    >>> is_subset(bobette, modified_bobette)
    Traceback (most recent call last):
      File "/usr/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest artemis.utils.is_subset[3]>", line 1, in <module>
        is_subset(bobette, bob)
      File "/home/antoine/dev/artemis/artemis/utils.py", line 159, in is_subset
        assert k in dict2
    AssertionError: assert 3 == 'changed'

    >>> is_subset(modified_bobette, bobette)
    Traceback (most recent call last):
      File "/usr/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest artemis.utils.is_subset[3]>", line 1, in <module>
        is_subset(bobette, bob)
      File "/home/antoine/dev/artemis/artemis/utils.py", line 159, in is_subset
        assert k in dict2
    AssertionError: assert 'changed' == 3
    """
    for k, v in dict1.iteritems():
        assert k in dict2

        if type(v) is dict:
            is_subset(v, dict2[k])
        else:
            assert v == dict2[k]


class PerfectComparator(object):
    """
    Classic comparator, all dict must be perfectly equals
    """
    @staticmethod
    def compare(response, ref):
        return check_equals(response, ref)


class SubsetComparison(object):
    """
    All element in the reference must be in the new response

    It tests that the api is always retro compatible (there can be more stuff, but never less)
    """
    @staticmethod
    def compare(response, ref):
        return is_subset(ref, response)


class Checker(object):
    """
    Navitia Response checker

    provides 2 methods:
    - one to filter the navitia response
    - one to compare the filtered response
    """
    def __init__(self, filter, comparator=PerfectComparator()):
        self._filter = filter
        self._comparator = comparator

    def filter(self, *args, **kwargs):
        return self._filter.filter(*args, **kwargs)

    def compare(self, *args, **kwargs):
        return self._comparator.compare(*args, **kwargs)


def launch_exec(cmd, additional_env=None):
    """
    Launch an exec with args, log the outputs
    return a tuple with (return code, process)
    the process can be used for example to kill the process later
    """
    logger = logging.getLogger(__name__)
    logger.debug('Launching ' + cmd)

    fdr, fdw = os.pipe()
    new_env = os.environ.copy()
    if additional_env:
        for k, v in additional_env.iteritems():
            new_env[k] = v
    try:
        proc = subprocess.Popen(cmd.split(' '), stderr=fdw,
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
