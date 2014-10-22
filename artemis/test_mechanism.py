import hashlib
import inspect
import logging
import os
import psycopg2
import re
import json
import time
import utils
import zipfile
from configuration_manager import config

# regexp used to identify a test method (simplified version of nose)
_test_method_regexp = re.compile("^(test_.*|.*_test)$")

_tyr = config['TYR_DIR'] + "/manage.py"
_tyr_config_file = config['TYR_DIR'] + "/settings.py"


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

def zip_path(dataset):
    p = config['ZIP_FILE_PATH_LAYOUT']
    return p.format(dataset=dataset)

class ArtemisTestFixture:
    """
    Mother class for all integration tests
    """

    def setup(self):
        """
        setup function called before each test

        Note: py.test does not want to collect class with custom constructor,
        so we init the class in the setup
        """
        logging.getLogger(__name__).warn("setup before function")
        self.api_call_by_params = {}  # key is md5 of url, val is the number of call

    @classmethod
    def setup_class(cls):
        """
        Method called once before running the tests of the fixture

        Launch all necessary services to have a running navitia solution
        """
        logging.getLogger(__name__).warn("Initing the tests {}, let's deploy!"
                                         .format(cls.__name__))

        cls.run_additional_service()

        cls.remove_data()

        cls.update_data()

        cls.read_data()

        cls.pop_krakens()  # this might be removed if tyr manage it (in the read_data process)

        cls.pop_jormungandr()

    @classmethod
    def update_data(cls):
        """
        if new dataset exist we must unzip in data directory to consider in "read_data"
        """
        for data_set in cls.data_sets:
            logging.getLogger(__name__).info("updating data for {}".format(data_set))
            zip_filename = zip_path(data_set)
            if not os.path.exists(zip_filename):
                continue
            zip_file = zipfile.ZipFile(zip_filename)
            zip_file.extractall(path=dir_path(data_set))
            os.remove(zip_filename)

    @classmethod
    def teardown_class(cls):
        """
        Method called once after running the tests of the fixture.
        """
        logging.getLogger(__name__).info("Tearing down the tests {}, time to clean up"
                                         .format(cls.__name__))
        cls.kill_the_krakens()
        cls.kill_jormungandr()

    @classmethod
    def run_additional_service(cls):
        """
        run all services that have to be active for all tests
        """
        pass

    @classmethod
    def read_data(cls):
        """
        Read the different data given by Fusio
        launch the different readers (Fusio2Ed, osm2is, ...) and binarize the data

        All is left to tyr
        """
        #clean jormungandr database
        cls.clean_jormun_db()
        for data_set in cls.data_sets:
            logging.getLogger(__name__).info("reading data for {}".format(data_set))
            utils.launch_exec("{tyr} load_data {data_set} {data_set_dir}"
                              .format(tyr=_tyr,
                                      data_set=data_set,
                                      data_set_dir=dir_path(data_set)),
                              additional_env={'TYR_CONFIG_FILE': _tyr_config_file})

    @classmethod
    def clean_jormun_db(cls):
        logging.getLogger(__name__).info("cleaning jomrungandr database")
        conn = psycopg2.connect(config['JORMUNGANDR_DB'])
        try:
            cur = conn.cursor()
            tables = ['data_set', 'instance', 'job']

            logging.getLogger(__name__).info("query: TRUNCATE {} CASCADE ;".format(', '.join(tables)))
            cur.execute("TRUNCATE {} CASCADE ;".format(', '.join(tables)))

            #we add the instances in the table
            for data_set in cls.data_sets:
                cur.execute("INSERT INTO instance (name, is_free) VALUES ('{}', true);".format(data_set))

            conn.commit()
            logging.getLogger(__name__).info("query done")
        except:
            logging.getLogger(__name__).exception("problem with jormun db")
            conn.close()
            assert "problem while cleaning jormungandr db"
        conn.close()

    @classmethod
    def pop_krakens(cls):
        """
        launch all the kraken services
        """
        for data_set in cls.data_sets:
            logging.getLogger(__name__).info("launching the kraken {}".format(data_set))
            return_code, _ = utils.launch_exec('sudo {service} {kraken} start'.format(service=_kraken_wrapper, kraken=data_set))

            assert return_code == 0, "command failed"

    @classmethod
    def kill_the_krakens(cls):
        for data_set in cls.data_sets:
            logging.getLogger(__name__).info("killing the kraken {}".format(data_set))
            return_code, _ = utils.launch_exec('sudo {service} {kraken} stop'.format(service=_kraken_wrapper, kraken=data_set))

            assert return_code == 0, "command failed"

    @classmethod
    def pop_jormungandr(cls):
        """
        launch the front end
        """
        logging.getLogger(__name__).info("running jormungandr")
        # jormungandr is launched with apache
        ret, _ = utils.launch_exec('sudo service apache2 start')

        assert ret == 0, "cannot start apache"

        # to have better errors, we check at the beginning that all is right
        for data_set in cls.data_sets:

            #we have to let some time to kraken to load the data
            nb_try = 15
            current_region = None
            for i_try in range (0, nb_try):
                response, _ = utils.api("coverage/{r}".format(r=data_set))
                assert 'error' not in response, "problem with the region: {error}".format(error=response['error'])

                current_region = response.get('regions', [None])[0]
                #the region should be the one asked for
                assert current_region and current_region['id'] == data_set

                status = current_region['status']
                if status is not None and \
                    status != 'loading_data':  #should be corrected in kraken, status should only be loading_data
                    break

                logging.getLogger(__name__).info("{} still loading data, waiting a bit".format(current_region['id']))

                time.sleep(1)

            #and it should be running
            assert current_region['status'] == 'running', "region {r} KO, status={s}, \n full response={resp}".\
                format(r=data_set, s=current_region['status'], resp=response)

    @classmethod
    def kill_jormungandr(cls):
        logging.getLogger(__name__).info("killing jormungandr")
        ret, _ = utils.launch_exec('sudo service apache2 stop')

        assert ret == 0, "cannot stop apache"

    @classmethod
    def remove_data(cls):
        for data_set in cls.data_sets:
            logging.getLogger(__name__).info("deleting data for {}".format(
                data_set))
            try:
                os.remove(nav_path(data_set))
            except:
                logging.getLogger(__name__).exception("can't remove data.nav"
                                                      ".lz4")
                assert "problem while cleaning data"

    ###################################
    # wrappers around utils functions #
    ###################################

    def api(self, url, response_mask=None):
        """
        call the api and check against previous results

        the query is writen in a file
        """
        response, url = utils.api(url)

        filtered_response = utils.filter_dict(response, response_mask)

        filename = self._save_response(url, response, filtered_response)

        utils.compare_with_ref(filtered_response, filename, response_mask)

    def journey(self, _from, to, datetime, datetime_represents='departure',
                response_mask=utils.default_journey_mask, auto_from=None, auto_to=None, **kwargs):
        """
        syntaxic sugar around the journey api

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

        for k, v in kwargs.iteritems():
            query = "{query}&{k}={v}".format(query=query, k=k, v=v)

        if len(self.__class__.data_sets) == 1:
            # for tests with only one dataset, we directly use the region's journey API
            # Note: this shoudl not be mandatory, but since there are still bugs with the global journey API
            # we use this for the moment.
            query = "coverage/{region}/journeys?{q}".format(region=self.__class__.data_sets[0], q=query)

        self.api(query, response_mask)

    def _get_file_name(self, url):
        """
        create the name of the file for storing the query.

        the file is:

        {fixture_name}/{function_name}_{md5_on_url}(|_{call_number}).json

        if a custom_name is provided we take it, else we create a md5 on the url.
        a custom_name must be provided is the same call is done twice in the same test function
        """
        class_name = self.__class__.__name__  # we get the fixture name
        func_name = get_calling_test_function()

        call_id = hashlib.md5(str(url).encode()).hexdigest()

        #if we already called this url in the same method, we add a number
        key = (func_name, call_id)
        if key in self.api_call_by_params:
            call_id = "{call}_{number}".format(call=call_id, number=self.api_call_by_params[key])
            self.api_call_by_params[call_id] += 1
        else:
            self.api_call_by_params[call_id] = 1

        return "{fixture_name}/{function_name}_{specific_call_id}.json"\
            .format(fixture_name=class_name, function_name=func_name, specific_call_id=call_id)

    def _save_response(self, url, response, filtered_response):
        """
        save the response in a file and return the filename (with the fixture directory)
        """
        filename = self._get_file_name(url)
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
