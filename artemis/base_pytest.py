import os
import json
import requests
import inspect
from artemis import default_checker, utils
from artemis.configuration_manager import config
import difflib
import sys
import six
import pytest
import logging
from collections import defaultdict
import docker
import tarfile
import zipfile
from retrying import retry


if six.PY3: # case using python 3
    from enum import Enum

if six.PY2: # case using python 2
    from aenum import Enum


class Colors(Enum):
    RED = '\033[91m'
    GREEN = '\033[92m'
    PINK = '\033[95m'
    DEFAULT = '\033[0m'


logger = logging.getLogger(__name__)

_kirin_api = config['KIRIN_API']


def print_color(line, color=Colors.DEFAULT):
    """console print, with color"""
    sys.stdout.write('{}{}{}'.format(color.value, line, Colors.DEFAULT.value))

# TODO: Move in utils
def get_calling_test_function():
    """
    return the calling test method.

    go back up the stack until a method with test in the name

    Used here to find the name of the coverage
    """
    for m in inspect.stack():
        method_name = m[3]  # m is a tuple and the 4th elt is the name of the function
        if utils._test_method_regexp.match(method_name):
            return method_name

    #a test method has to be found by construction, if none is found there is a problem
    raise KeyError("impossible to find the calling test method")

def get_ire_data(name):
    """
    return an IRE input as string
    the name must be the name of a file in tests/fixtures
    """
    _file = os.path.join(os.path.dirname(__file__), 'tests', 'fixtures', name)
    with open(_file, "r") as ire:
        return ire.read()
        
class ArtemisTestFixture(object):

    dataset_binarized = []

    # Name of the docker container from the docker-compose
    # TODO: Needs to be common with docker-compose.yml
    tyr_worker_container_name = 'navitiadockercompose_tyr_worker_1'

    @pytest.fixture(scope='function', autouse=True)
    def before_each_test(self):
        """
        setup function called before each test

        Note: py.test does not want to collect class with custom constructor,
        so we init the class in the setup
        """
        self.test_counter = defaultdict(int)

    @classmethod
    @pytest.yield_fixture(scope='class', autouse=True)
    def manage_data(cls):

        for data_set in cls.data_sets:
            if data_set.name in cls.dataset_binarized:
                logger.info("binarization dataset {} has been done, skipping....".format(data_set))
                continue
            cls.remove_data_by_dataset(data_set)
            cls.update_data_by_dataset(data_set)
            cls.dataset_binarized.append(data_set.name)

    @classmethod
    def remove_data_by_dataset(cls, data_set):
        file_path = '/srv/ed/output/{}.nav.lz4'.format(data_set.name)
        logger.info('path to volume from container: ' + file_path)
        client = docker.from_env()
        container = client.containers.get(cls.tyr_worker_container_name)
        container.exec_run('rm ' + file_path)

    @classmethod
    def update_data_by_dataset(cls, data_set):
        def get_last_coverage_loaded_time(cov):

            _response, _, _ = utils.request("coverage/{cov}/status".format(cov=cov))
            return _response.get('status', {}).get('last_load_at', "")

        # wait 5 min at most
        @retry(stop_max_delay=300000, wait_fixed=5000)
        def wait_for_kraken_reload(last_rt_data_loaded, cov):
            new_rt_data_loaded = get_last_coverage_loaded_time(cov)

            if last_rt_data_loaded == new_rt_data_loaded:
                raise Exception("kraken data is not loaded")
            return

        data_path = config['DATA_DIR']
        input_path = '{}/{}'.format(config['CONTAINER_DATA_INPUT_PATH'], data_set.name)

        logger.info("updating data for {}".format(data_set.name))

        # opening the container as client
        client = docker.from_env()
        container = client.containers.get(cls.tyr_worker_container_name)
        container.exec_run('mkdir ' + input_path)

        # Have the last reload time by Kraken
        last_reload_time = get_last_coverage_loaded_time(cov=data_set.name)
        logger.info('last loaded time : ' + str(last_reload_time))

        # put the fusio data
        fusio_path = '{}/{}/fusio'.format(data_path, data_set.name)
        fusio_databases_file = fusio_path + '/{}.zip'.format(data_set.name)

        if os.path.exists(fusio_path):
            logger.info('putting Fusio data : {}'.format(fusio_path))
            file_list = []
            # get all the files names from fusio
            for file in os.listdir(fusio_path):
                if file.endswith('.txt'):
                    file_list.append(file)
            # put them into a zip
            with zipfile.ZipFile('{}/{}.zip'.format(fusio_path, data_set.name), 'w') as zip:
                for name in file_list:
                    zip.write('{}/{}'.format(fusio_path, name), arcname=name)
            # put the zip into a tar
            with tarfile.open("./sample1.tar", "w") as tar:
                for name in [fusio_databases_file]:
                    tar.add(name, arcname='{}.zip'.format(data_set.name))
            # send the tar to the volume
            with open('./sample1.tar', 'rb') as f:
                container.put_archive(input_path, f.read())
        else:
            logger.warning('Fusio path does not exist : {}'.format(fusio_path))

        # put the osm data
        osm_path = '{}/{}/osm'.format(data_path, data_set.name)
        osm_file_name = ''
        if os.path.exists(osm_path):
            logger.info('putting osm data : {}'.format(osm_path))

            # get the osm file name
            for f in os.listdir(osm_path):
                if f.endswith('.pbf'):
                    osm_file_name += f
            osm_file = osm_path + '/' + osm_file_name

            # put the osm file in a tar
            with tarfile.open("./sample1.tar", "w") as tar:
                for name in [osm_file]:
                    tar.add(name, arcname=osm_file_name)
            # send the tar to volume
            with open('./sample1.tar', 'rb') as f:
                container.put_archive(input_path, f.read())
        else:
            logger.warning('osm path does not exist : {}'.format(osm_path))

        # put the osm data
        geopal_path = '{}/{}/geopal'.format(data_path, data_set.name)
        geopal_file_name = ''
        if os.path.exists(geopal_path):
            logger.info('putting osm data : {}'.format(geopal_path))

            # get the osm file name
            for f in os.listdir(geopal_path):
                if f.endswith('.pbf'):
                    geopal_file_name += f
            geopal_file = geopal_path + '/' + geopal_file_name

            # put the osm file in a tar
            with tarfile.open("./sample1.tar", "w") as tar:
                for name in [geopal_file]:
                    tar.add(name, arcname=osm_file_name)
            # send the tar to volume
            with open('./sample1.tar', 'rb') as f:
                container.put_archive(input_path, f.read())
        else:
            logger.warning('geopal file path does not exist : {}'.format(geopal_path))

        # Wait until data is reloaded
        wait_for_kraken_reload(last_reload_time, data_set.name)

    #####################################################################################################

    def send_ire(self, ire_name):
        print("IRE FILE = {} :\n{}".format(ire_name, get_ire_data(ire_name)))
        print("Request to : {}".format(_kirin_api+'/ire'))
        r = requests.post(_kirin_api+'/ire',
                      data=get_ire_data(ire_name).encode('UTF-8'),
                      headers={'Content-Type': 'application/xml;charset=utf-8'})
        r.raise_for_status()
        
    @retry(stop_max_delay=25000, wait_fixed=500)
    def get_last_rt_loaded_time(self, cov):
        _res, _, status_code = utils.request("coverage/{cov}/status".format(cov=cov))

        if status_code == 503:
            raise Exception("Navitia is not available")

        return _res.get('status', {}).get('last_rt_data_loaded', object())

    @retry(stop_max_delay=25000, wait_fixed=500)
    def wait_for_rt_reload(self, last_rt_data_loaded, cov):
        rt_data_loaded = self.get_last_rt_loaded_time(cov)

        if last_rt_data_loaded == rt_data_loaded:
            raise Exception("real time data not loaded")

    #####################################################################################################
    
    def request_compare(self, url):

        # creating the url
        query = config['URL_JORMUN'] + '/v1/coverage/' + str(self.data_sets[0]) + '/' + url

        # Get the json answer of the request (it is just a string here)
        raw_response = requests.get(query)

        # Transform the string into a dictionary
        dict_resp = json.loads(raw_response.text)

        # Comparing my response and my reference
        compare_with_ref(self, dict_resp)

    def get_file_name(self):
        """
        Get second half of the path to the artemis reference file
        """
        mro = inspect.getmro(self.__class__)
        class_name = "Test{}".format(mro[1].__name__)
        # TODO: needs to be configurable
        scenario = 'new_default'

        func_name = get_calling_test_function()
        test_name = '{}/{}/{}'.format(class_name, scenario, func_name)
        file_name = "{}.json".format(test_name)
        return file_name

    def journey(self, _from, to, datetime,
                datetime_represents='departure',
                first_section_mode=[], last_section_mode=[],
                **kwargs):
        """
        This function is coming from the test_mechanism.py file.
        We only use the part that generates the url.
        Other parts are calling test that fail because we do not have the whole navitia running.
        Thus, we do not need the "self" parameter, and response_checker is set to None.
        We have also added parts of other functions into it.
        Therefore, we only need to call journey and all the test are done from inside.
        """

        # Creating the URL with all the parameters for the query
        assert datetime
        query = "from={real_from}&to={real_to}&datetime={date}&datetime_represents={represent}". \
            format(date=datetime, represent=datetime_represents,
                   real_from=_from, real_to=to)
        for mode in first_section_mode:
            query = '{query}&first_section_mode[]={mode}'.format(query=query, mode=mode)

        for mode in last_section_mode:
            query = '{query}&last_section_mode[]={mode}'.format(query=query, mode=mode)

        for k, v in six.iteritems(kwargs):
            query = "{query}&{k}={v}".format(query=query, k=k, v=v)

        # launching request dans comparing
        self.request_compare('journeys?' + query)


def compare_with_ref(self, response, response_checker=default_checker.default_journey_checker):
    """
    This function takes the response (which is a dictionary) and compare it to the reference
    It first goes finding the reference
    Then filters both ref and resp
    Finaly it compares them
    """

    def ref_resp2files():

        # save reference
        with open(full_file_name_ref, 'w') as reference_text:
            reference_text.write(json_filtered_reference)
        # save response
        with open(full_file_name_resp, 'w') as response_text:
            response_text.write(json_filtered_response)

    def print_diff():

        # open reference
        with open(full_file_name_ref) as reference_text:
            reference = reference_text.readlines()
        # open response
        with open(full_file_name_resp) as response_text:
            response = response_text.readlines()

        # Print failed test name
        print_color('\n\n' + str(file_name) + ' failed :' + '\n\n', Colors.PINK)

        # PriTestFixturent differences between ref and resp in console
        for line in difflib.unified_diff(reference, response):
            if line[0] == '+':
                print_color(line, Colors.GREEN)
            elif line[0] == '-':
                print_color(line, Colors.RED)
            else:
                sys.stdout.write(line)

    ### Get the reference

    # Create the file name
    filename = self.get_file_name()

    # Add path to artemis references
    relative_path_ref = config['REFERENCE_FILE_PATH']
    filepath = os.path.join(relative_path_ref, filename)
    assert os.path.isfile(filepath), "{} is not a file".format(filepath)

    with open(filepath, 'r') as f:
        raw_reference = f.read()

    # Transform the string into a dictionary
    dict_ref = json.loads(raw_reference)

    # Get only the full_response part from the ref
    ref_full_response = dict_ref['full_response']


    ### Filtering ref end resp

    # Filtering with the checker
    filtered_reference = response_checker.filter(ref_full_response)

    # Filtering the answer. (We compare to a reference also filtered with the same filter)
    filtered_response = response_checker.filter(response)

    ### Create a json layout string
    json_filtered_reference = json.dumps(filtered_reference, indent=4)
    json_filtered_response = json.dumps(filtered_response, indent=4)

    ### Compare response and reference
    compare_result = response_checker.compare(filtered_response, filtered_reference)

    ### If not resp and ref different
    if not compare_result:

        # find name of test
        file_path = str(self.get_file_name())
        file_name = file_path.split('/')[-1]
        file_name = file_name[:-5]

        # create a folder
        dir_path = config['RESPONSE_FILE_PATH']
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # create path to ref and resp
        full_file_name_ref = dir_path + '/reference_' + file_name + '.txt'
        full_file_name_resp = dir_path + '/response_' + file_name + '.txt'

        # Save resp and ref as txt files in folder named outputs
        ref_resp2files()

        # Print difference in console
        print_diff()

    assert compare_result
