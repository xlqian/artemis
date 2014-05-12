import hashlib
import inspect
import logging
import os
import re
import utils
from configuration_manager import config



_test_method_regexp = re.compile("^(test_.*|.*_test)$")

class ArtemisTestFixture:
    """
    Mother class for all integration tests
    """

    def init(self):
        """
        py.test does not want to collect class with custom constructor,
        so we init the class in the setup
        """
        self.api_call_by_function = {}

    def setup(self):
        self.init()
        logging.getLogger(__name__).info("Initing the tests {}, let's deploy!"
                                         .format(self.__class__.__name__))
        self.run_tyr()

        self.run_additional_service()

        self.read_data()

        self.pop_krakens()  # this might be removed if tyr manage it (in the read_data process)

        self.pop_jormungandr()

    def teardown(self):
        logging.getLogger(__name__).info("Tearing down the tests {}, time to clean up"
                                         .format(self.__class__.__name__))

    def run_tyr(self):
        """
        run tyr
        tyr is the conductor of navitia.
        """
        pass

    def run_additional_service(self):
        """
        run all services that have to be active for all tests
        """
        pass

    def read_data(self):
        """
        Read the different data given by Fusio
        launch the different readers (Fusio2Ed, osm2is, ...) and binarize the data
        """
        pass

    def pop_krakens(self):
        pass

    def pop_jormungandr(self):
        """
        launch the front end
        """
        pass

    ###################################
    # wrappers around utils functions #
    ###################################

    def api(self, url):
        """
        call the api and check against previous results

        the query is writen in a file
        """
        response = utils.api(url)

        self.save_response(url, response)

    def get_file_name(self, url):
        """
        create the name of the file for storing the query.

        the file is:

        {fixture_name}/{function_name}_{md5_on_url}(|_{call_number}).json

        if a custom_name is provided we take it, else we create a md5 on the url.
        a custom_name must be provided is the same call is done twice in the same test function
        """
        class_name = self.__class__.__name__  # we get the fixture name
        func_name = self.get_calling_test_function()

        call_id = hashlib.md5(str(url).encode()).hexdigest()

        #if we already called this url in the same method, we add a number
        key = (func_name, call_id)
        if key in self.api_call_by_function:
            call_id = "{call}_{number}".format(call=call_id, number=self.api_call_by_function[key])
            self.api_call_by_function[key] += 1
        else:
            self.api_call_by_function[key] = 1

        return "{fixture_name}/{function_name}_{specific_call_id}.json"\
            .format(fixture_name=class_name, function_name=func_name, specific_call_id=call_id)

    def get_calling_test_function(self):
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

    def save_response(self, url, response):
        filename = os.path.join(config['RESPONSE_FILE_PATH'], self.get_file_name(url))
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))

        file_ = open(filename, 'w')
        file_.write(response)
        file_.close()
