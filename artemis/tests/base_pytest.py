import inspect
from artemis import default_checker, utils
import os
from flask import json
import requests
import inspect
import re
from artemis.configuration_manager import config

def get_calling_test_function():
    """
    return the calling test method.

    go back up the stack until a method with test in the name
    """
    for m in inspect.stack():
        method_name = m[3]  # m is a tuple and the 4th elt is the name of the function
        if utils._test_method_regexp.match(method_name):
            return method_name

    #a test method has to be found by construction, if none is found there is a problem
    raise KeyError("impossible to find the calling test method")

class TestFixture(object):

    def get_file_name(self):
        mro = inspect.getmro(self.__class__)
        class_name = "{}".format(mro[0].__name__)
        scenario = 'new_default'

        func_name = get_calling_test_function()
        test_name = '{}/{}/{}'.format(class_name, scenario, func_name)
        file_name = "{}.json".format(test_name)
        print file_name
        return file_name

    def journey(self, _from, to, datetime,
                datetime_represents='departure',
                auto_from=None, auto_to=None,
                first_section_mode=[], last_section_mode=[],
                **kwargs):
        """
        This function is comming from the test_mechanism.py file.
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

        for k, v in kwargs.iteritems():
            query = "{query}&{k}={v}".format(query=query, k=k, v=v)

        # full URL concatenation
        query = config['URL_JORMUN'] + query

        # Get the json answer of the request (it is just a string here)
        raw_response = requests.get(query)

        # Transform the string into a dictionary
        dict_resp = json.loads(raw_response.text)

        # Comparing my response and my reference
        compare_with_ref(self, dict_resp)

def compare_with_ref(self, response,
                        response_checker=default_checker.default_journey_checker):
    """
    This function take the response (which is a dictionary) and compare it to a the reference
    It first goes finding the reference
    Then filters both ref and resp
    Finaly it compares them

    """
    def save_ref_resp_as_files():
        with open('reference.txt', 'w') as reference_text:
            reference_text.write(json.dumps(filtered_reference, indent=4))

        with open('response.txt', 'w') as response_text:
            response_text.write(json.dumps(filtered_response, indent=4))

    ### Get the reference

    # Create the file name
    filename = self.get_file_name()

    # Add path to artemis references
    # config = flask_conf.Config(os.path.dirname(os.path.realpath(__file__)))
    filepath = os.path.join(config['PATH_REF'], filename)

    assert os.path.isfile(filepath)
    with open(filepath, 'r') as f:
        raw_reference = f.read()
    #print("reference : ", raw_reference)

    # Transform the string into a dictionary
    dict_ref = json.loads(raw_reference)

    # Get only the full_response part from the ref
    ref_full_response = dict_ref['full_response']


    ### Filtering ref end resp

    # Filtering with the checker
    filtered_reference = response_checker.filter(ref_full_response)

    # Filtering the answer. (We compare to a reference also filtered with the same filter)
    filtered_response = response_checker.filter(response)
    #print(filtered_response)


    # This part is only to check ref and resp content by saving them into files
    #save_ref_resp_as_files()

    ### Compare response and reference
    response_checker.compare(filtered_response, filtered_reference)