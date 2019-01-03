import logging
import inspect
import requests

import artemis.utils as utils

from artemis.configuration_manager import config

logger = logging.getLogger(__name__)


class CommonTestFixture(object):
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

        func_name = utils.get_calling_test_function()
        test_name = '{}/{}/{}'.format(class_name, scenario, func_name)

        self.test_counter[test_name] += 1

        if self.test_counter[test_name] > 1:
            return "{}_{}.json".format(test_name, self.test_counter[test_name] - 1)
        else:
            return "{}.json".format(test_name)

    def send_cots(self, cots_file_name):
        r = requests.post(config['KIRIN_API'] + '/cots',
                          data=utils.get_rt_data(cots_file_name).encode('UTF-8'),
                          headers={'Content-Type': 'application/json;charset=utf-8'})
        r.raise_for_status()

