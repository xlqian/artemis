from collections import defaultdict
import inspect
import logging
import os
import shutil
import psycopg2
import re
import json
import time
import pytest
from retrying import Retrying, retry, RetryError
from artemis import default_checker
from artemis import utils
import requests
from artemis.configuration_manager import config
import datetime

# regexp used to identify a test method (simplified version of nose)
_test_method_regexp = re.compile("^(test_.*|.*_test)$")

_tyr = config['TYR_DIR'] + "/manage.py"
_tyr_config_file = config['TYR_DIR'] + "/settings.py"

_kirin_api = config['KIRIN_API']
#to limit the permissions of the jenkins user on the artemis platform, we create a proxy for all kraken services
_kraken_wrapper = '/usr/local/bin/kraken_service_wrapper'


def get_calling_test_function():
    """
    return the calling test method.

    go back up the stack until a method with test in the name
    """
    for m in inspect.stack():
        method_name = m[3]  # m is a tuple and the 4th elt is the name of the function
        if _test_method_regexp.match(method_name):
            return method_name

    #a test method has to be found by construction, if none is found there is a problem
    raise KeyError("impossible to find the calling test method")


def dir_path(dataset):
    p = config['DATASET_PATH_LAYOUT']
    return p.format(dataset=dataset)


def nav_path(dataset):
    p = config['NAV_FILE_PATH_LAYOUT']
    return p.format(dataset=dataset)


def new_fusio_files_path(dataset):
    p = config['NEW_FUSIO_FILE_PATH_LAYOUT']
    return p.format(dataset=dataset.upper())


def get_ire_data(name):
    """
    return an IRE input as string
    the name must be the name of a file in tests/fixtures
    """
    _file = os.path.join(os.path.dirname(__file__), 'tests', 'fixtures', name)
    with open(_file, "r") as ire:
        return ire.read()

# given a cursor on a db, and table names separated by a comma (ex: "tata, toto, titi")
def truncate_tables(cursor, table_names_string):
    logging.getLogger(__name__).debug("query db: TRUNCATE {} CASCADE ;".format(table_names_string))
    cursor.execute("TRUNCATE {} CASCADE ;".format(table_names_string))


class DataSet(object):
    def __init__(self,
                 name,
                 reload_timeout=datetime.timedelta(minutes=2),
                 fixed_wait=datetime.timedelta(seconds=1),
                 scenario='default'):
        self.name = name
        self.scenario = scenario
        self.reload_timeout = reload_timeout.total_seconds()
        self.fixed_wait = fixed_wait.total_seconds()

    def __str__(self):
        return self.name


def set_scenario(config):
    def deco(cls):
        cls.data_sets = []
        for c in cls.__bases__:
            if hasattr(c, "data_sets"):
                for dataset in c.data_sets:
                    cls.data_sets.append(DataSet(dataset.name,
                                                 datetime.timedelta(minutes=2),
                                                 datetime.timedelta(seconds=1),
                                                 dataset.scenario))
        if config:
            for dataset in cls.data_sets:
                conf = config.get(dataset.name, None)
                if conf:
                    dataset.scenario = conf.get("scenario", "default")
        return cls
    return deco


def kraken_status(data_set):
    response, _, _ = utils.request("coverage/{r}".format(r=data_set.name))
    assert 'error' not in response, "problem with the region: {error}".format(error=response['error'])

    current_region = response.get('regions', [None])[0]
    #the region should be the one asked for
    assert current_region and current_region['id'] == data_set.name

    return current_region['status']


class ArtemisTestFixture:
    """
    Mother class for all integration tests
    """
    dataset_binarized = []
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
    def my_method_setup(cls, request):
        """
        method called once for each fixture

        Handle init and teardown of the fixture
        """
        logging.getLogger(__name__).debug("Setting up the tests {}".format(cls.__name__))
        cls.init_fixture(skip_bina=request.config.getvalue("skip_bina"),
                         journey_full_response_comparison_mode=request.config.getvalue("hard_journey_check"),
                         check_ref=request.config.getvalue("check_ref"))

        logging.getLogger(__name__).debug("Running the tests {}".format(cls.__name__))
        yield

        if not request.config.getvalue("check_ref"):
            logging.getLogger(__name__).debug("Cleaning up the tests {}".format(cls.__name__))
            cls.clean_fixture()

    @classmethod
    def init_fixture(cls, skip_bina, journey_full_response_comparison_mode, check_ref):
        """
        Method called once before running the tests of the fixture

        Launch all necessary services to have a running navitia solution
        :param skip_bina to use the already done binarization
        :param journey_full_response_comparison_mode if set to True will compare the journeys
        on the full_response with the no regression mode (like the other apis)
        :param check_ref to check only consistency of reference files
        This should be used only occasionally as the journey response are prone to changes
        """
        # we store the variable to use it a test time
        if journey_full_response_comparison_mode:
            logging.getLogger(__name__).warning("Full journeys comparison activated")
        cls.journey_full_response_comparison_mode = journey_full_response_comparison_mode
        cls.check_ref = check_ref

        if check_ref:
            return

        cls.kill_jormungandr()

        cls.run_additional_service()

        # clean kirin database
        cls.clean_kirin_db()

        cls.manage_data(skip_bina)

        cls.pop_krakens()

        cls.pop_jormungandr()

    @classmethod
    def manage_data(cls, skip_bina):

        cls.clean_jormun_db()

        if skip_bina:
            logging.getLogger(__name__).info("skipping binarization")
            return

        for data_set in cls.data_sets:
            if data_set.name in cls.dataset_binarized:
                logging.getLogger(__name__).debug("binarization dataset {} has been done, skipping....".format(data_set))
                continue
            cls.remove_data_by_dataset(data_set)
            cls.update_data_by_dataset(data_set)
            cls.read_data_by_dataset(data_set)
            cls.dataset_binarized.append(data_set.name)

    @classmethod
    def remove_data_by_dataset(cls, data_set):
        logging.getLogger(__name__).debug("deleting data for {}".format(data_set.name))
        try:
            if os.path.exists(utils.nav_path(data_set.name)):
                os.remove(utils.nav_path(data_set.name))
        except:
            logging.getLogger(__name__).exception("can't remove data.nav.lz4")

    @classmethod
    def update_data_by_dataset(cls, data_set):
        fusio_databases_file = utils.new_fusio_files_path(data_set.name)
        if not os.path.exists(fusio_databases_file):
            return

        logging.getLogger(__name__).debug("updating data for {}".format(data_set.name))

        #we copy the file to update the reference data
        shutil.move(fusio_databases_file, os.path.join(utils.instance_data_path(data_set.name), 'fusio/databases.zip'))

    @classmethod
    def read_data_by_dataset(cls, data_set):
        logging.getLogger(__name__).debug("reading data for {}".format(data_set.name))
        # we'll read all subdir
        data_path = utils.instance_data_path(data_set.name)

        data_dirs = [os.path.join(data_path, sub_dir_name)
                     for sub_dir_name in os.listdir(data_path)
                     if os.path.isdir(os.path.join(data_path, sub_dir_name))]

        logging.getLogger(__name__).debug("loading {}".format(data_dirs))
        utils.launch_exec("{tyr} load_data {data_set} {data_set_dir}"
                          .format(tyr=_tyr,
                                  data_set=data_set.name,
                                  data_set_dir=','.join(data_dirs)),
                          additional_env={'TYR_CONFIG_FILE': _tyr_config_file})

    @classmethod
    def clean_fixture(cls):
        """
        Method called once after running the tests of the fixture.
        """
        logging.getLogger(__name__).debug("Tearing down the tests {}, time to clean up"
                                          .format(cls.__name__))
        cls.kill_the_krakens()

    @classmethod
    def run_additional_service(cls):
        """
        run all services that have to be active for all tests
        """
        pass

    @classmethod
    def clean_jormun_db(cls):
        logging.getLogger(__name__).debug("cleaning jormungandr database")
        conn = psycopg2.connect(config['JORMUNGANDR_DB'])
        try:
            cur = conn.cursor()
            tables = ['data_set', 'instance', 'job']

            truncate_tables(cur, ', '.join(tables))

            #we add the instances in the table
            for data_set in cls.data_sets:
                cur.execute("INSERT INTO instance (name, is_free, is_open_data, scenario) VALUES ('{}', true, false, '{}');".format(data_set.name, data_set.scenario))

            conn.commit()
            logging.getLogger(__name__).debug("query done")
        except:
            logging.getLogger(__name__).exception("problem with jormun db")
            conn.close()
            assert False, "problem while cleaning jormungandr db"
        conn.close()

    @classmethod
    def pop_krakens(cls):
        """
        launch all the kraken services
        """
        if cls.check_ref:
            return

        for data_set in cls.data_sets:
            logging.getLogger(__name__).debug("launching the kraken {}".format(data_set.name))
            return_code, _ = utils.launch_exec('sudo {service} {kraken} start'.format(service=_kraken_wrapper, kraken=data_set.name))

            assert return_code == 0, "command failed"

    @classmethod
    def kill_the_krakens(cls):
        if cls.check_ref:
            return

        for data_set in cls.data_sets:
            logging.getLogger(__name__).debug("killing the kraken {}".format(data_set.name))
            return_code, _ = utils.launch_exec('sudo {service} {kraken} stop'.format(service=_kraken_wrapper, kraken=data_set.name))

            assert return_code == 0, "command failed"

    @classmethod
    def pop_jormungandr(cls):
        """
        launch the front end
        """
        logging.getLogger(__name__).debug("running jormungandr")
        # jormungandr is launched with apache
        utils.launch_exec('sudo service apache2 status')
        ret, _ = utils.launch_exec('sudo service apache2 start')
        utils.launch_exec('sudo service apache2 status')

        assert ret == 0, "cannot start apache"

        # to have better errors, we check at the beginning that all is right
        for data_set in cls.data_sets:

            # we wait a bit for the kraken to be started
            try:
                Retrying(stop_max_delay=data_set.reload_timeout * 1000,
                         wait_fixed=data_set.fixed_wait * 1000,
                         retry_on_result=lambda x: x != 'running') \
                    .call(kraken_status, data_set)
            except RetryError as e:
                assert False, "region {r} KO, status={s}".format(r=data_set.name, s=e.last_attempt.value)

    @classmethod
    def kill_jormungandr(cls):
        logging.getLogger(__name__).debug("killing jormungandr")
        utils.launch_exec('sudo service apache2 status')
        ret, _ = utils.launch_exec('sudo service apache2 stop')
        utils.launch_exec('sudo service apache2 status')

        assert ret == 0, "cannot stop apache"

    @classmethod
    def clean_kirin_db(cls):
        logging.getLogger(__name__).debug("cleaning kirin database")
        conn = psycopg2.connect(config['KIRIN_DB'])
        try:
            cur = conn.cursor()
            cur.execute("SELECT relname FROM pg_stat_user_tables WHERE relname != 'alembic_version';")
            tables = cur.fetchall()

            truncate_tables(cur, ', '.join(e[0] for e in tables))

            conn.commit()
            logging.getLogger(__name__).debug("query done")
        except:
            logging.getLogger(__name__).exception("problem with kirin db")
            conn.close()
            assert False, "problem while cleaning kirin db"
        conn.close()

    ###################################
    # wrappers around utils functions #
    ###################################

    def send_ire(self, ire_name):
        if self.check_ref:
            return

        requests.post(_kirin_api+'/ire',
                      data=get_ire_data(ire_name),
                      headers={'Content-Type': 'application/xml;charset=utf-8'})

    @retry(stop_max_delay=25000, wait_fixed=500)
    def get_last_rt_loaded_time(self, cov):
        if self.check_ref:
            return

        _res, _, status_code = utils.request("coverage/{cov}/status".format(cov=cov))

        if status_code == 503:
            raise Exception("Navitia is not available")

        return _res.get('status', {}).get('last_rt_data_loaded', object())

    @retry(stop_max_delay=25000, wait_fixed=500)
    def wait_for_rt_reload(self, last_rt_data_loaded, cov):
        if self.check_ref:
            return

        rt_data_loaded = self.get_last_rt_loaded_time(cov)

        if last_rt_data_loaded == rt_data_loaded:
            raise Exception("real time data not loaded")

    def api(self, url, response_checker=default_checker.default_checker):
        """
        used to check misc API

        NOTE: works only when one region is loaded for the moment (when needed change this)
        """
        if len(self.__class__.data_sets) == 1:
            full_url = "coverage/{region}/{url}".format(region=self.__class__.data_sets[0].name, url=url)

        return self._api_call(full_url, response_checker)

    def _api_call(self, url, response_checker):
        """
        call the api and check against previous results

        the query is writen in a file
        """
        if self.check_ref: # only check consistency
            filename = self._get_file_name()
            assert utils.check_reference_consistency(filename, response_checker)
            return

        response, url, _ = utils.request(url)

        filtered_response = response_checker.filter(response)

        filename = self._save_response(url, response, filtered_response)

        utils.compare_with_ref(filtered_response, filename, response_checker)

    def journey(self, _from, to, datetime, datetime_represents='departure',
                response_checker=default_checker.default_journey_checker,
                auto_from=None, auto_to=None,
                first_section_mode=[], last_section_mode=[],
                **kwargs):
        """
        syntactic sugar around the journey api

        auto_from and auto_to are used to access the autocomplete api

        TODO: example

        TODO: just forward args to the 'request' module without creating a string
        """
        real_from = self.call_autocomplete(auto_from) if auto_from else _from
        assert real_from

        real_to = self.call_autocomplete(auto_to) if auto_to else to
        assert real_to

        assert datetime
        query = "from={real_from}&to={real_to}&datetime={date}&datetime_represents={represent}".\
            format(date=datetime, represent=datetime_represents,
                   real_from=real_from, real_to=real_to)
        for mode in first_section_mode:
            query = '{query}&first_section_mode[]={mode}'.format(query=query, mode=mode)

        for mode in last_section_mode:
            query = '{query}&last_section_mode[]={mode}'.format(query=query, mode=mode)

        for k, v in kwargs.iteritems():
            query = "{query}&{k}={v}".format(query=query, k=k, v=v)
        if len(self.__class__.data_sets) == 1:
            # for tests with only one dataset, we directly use the region's journey API
            # Note: this should not be mandatory, but since there are still bugs with the global journey API
            # we use this for the moment.
            query = "coverage/{region}/journeys?{q}".format(region=self.__class__.data_sets[0].name, q=query)

        if self.journey_full_response_comparison_mode:
            # we want to compare the journeys very thoroughly, check the non regression on the full_response
            response_checker = default_checker.journeys_retrocompatibility_checker

        self._api_call(query, response_checker)

    def _get_file_name(self):
        """
        create the name of the file for storing the query.

        the file is:

        {fixture_name}/{function_name}_{md5_on_url}(|_{call_number}).json

        if a custom_name is provided we take it, else we create a md5 on the url.
        a custom_name must be provided is the same call is done twice in the same test function
        """
        mro = inspect.getmro(self.__class__)
        class_name = "Test{}".format(mro[1].__name__)
        scenario = mro[0].data_sets[0].scenario

        func_name = get_calling_test_function()
        test_name = '{}/{}/{}'.format(class_name, scenario, func_name)

        self.test_counter[test_name] += 1

        if self.test_counter[test_name] > 1:
            return "{}_{}.json".format(test_name, self.test_counter[test_name] - 1)
        else:
            return "{}.json".format(test_name)

    def _save_response(self, url, response, filtered_response):
        """
        save the response in a file and return the filename (with the fixture directory)
        """
        filename = self._get_file_name()
        file_complete_path = os.path.join(config['RESPONSE_FILE_PATH'], filename)
        if not os.path.exists(os.path.dirname(file_complete_path)):
            os.makedirs(os.path.dirname(file_complete_path))

        #to ease debug, we add additional information to the file
        #only the response elt will be compared, so we can add what we want (additional flags or whatever)
        enhanced_response = {"query": url,
                             "response": filtered_response,
                             "full_response": response}

        file_ = open(file_complete_path, 'w')
        file_.write(json.dumps(enhanced_response, indent=2))
        file_.close()

        return filename

    def call_autocomplete(self, place):
        #TODO!
        pass


def dataset(datasets):
    """
    decorator giving class attribute 'data_sets'

    each test should have this decorator to make clear the data set used for the tests
    """

    def deco(cls):
        cls.data_sets = datasets
        return cls
    return deco
