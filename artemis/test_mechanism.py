import hashlib
import inspect
import logging
import os
import re
import shutil
import json
import utils
from configuration_manager import config

# regexp used to identify a test method (simplified version of nose)
_test_method_regexp = re.compile("^(test_.*|.*_test)$")


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

        cls.run_tyr()

        cls.run_additional_service()

        cls.read_data()

        cls.pop_krakens()  # this might be removed if tyr manage it (in the read_data process)

        cls.pop_jormungandr()

    @classmethod
    def teardown_class(cls):
        """
        Method called once after running the tests of the fixture.
        """
        logging.getLogger(__name__).info("Tearing down the tests {}, time to clean up"
                                         .format(cls.__name__))

    @classmethod
    def run_tyr(cls):
        """
        run tyr
        tyr is the conductor of navitia.
        """
        pass

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
        """
        pass

    @classmethod
    def pop_krakens(cls):
        """
        launch all the kraken services
        """
        pass

    @classmethod
    def pop_jormungandr(cls):
        """
        launch the front end
        """
        pass

    ###################################
    # wrappers around utils functions #
    ###################################

    def api(self, url, response_mask=None):
        """
        call the api and check against previous results

        the query is writen in a file
        """
        complete_url = utils._api_current_root_point + url

        response, url = utils.api(complete_url)

        filtered_response = utils.filter_dict(response, response_mask)

        filename = self._save_response(url, response, filtered_response)

        utils.compare_with_ref(filtered_response, filename)

    def journey(self, _from, to, datetime, datetime_represents='departure',
                response_mask=utils.default_journey_mask, auto_from=None, auto_to=None, **kwargs):
        """
        syntaxic sugar around the journey api

        auto_from and auto_to are used to access the autocomplete api

        TODO: example
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

        self.journey_url(query, response_mask)

    def journey_url(self, url, response_mask=utils.default_journey_mask):
        self.api("journeys?" + url, response_mask)

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
