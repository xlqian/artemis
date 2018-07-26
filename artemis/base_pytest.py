import os
import json
import requests
import inspect
from artemis import default_checker, utils
from artemis.configuration_manager import config
import difflib
import sys

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

class TestFixture(object):

    def get_file_name(self):
        """
        Get second half of the path to the artemis reference file
        """
        mro = inspect.getmro(self.__class__)
        class_name = "{}".format(mro[0].__name__)
        scenario = 'new_default'

        func_name = get_calling_test_function()
        test_name = '{}/{}/{}'.format(class_name, scenario, func_name)
        file_name = "{}.json".format(test_name)
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
        query = config['URL_JORMUN'] + '/v1/coverage/' + str(self.data_sets[0]) + '/journeys?' + query

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
        sys.stdout.write('\033[95m' + '\n\n' +  str(file_name) + ' failed :' + '\033[0m' + '\n\n')

        # Print differences between ref and resp in console
        for line in difflib.unified_diff(reference, response):
            if line[0] == '+':
                sys.stdout.write('\033[92m' + line + '\033[0m') # Print in green
            elif line[0] == '-':
                sys.stdout.write('\033[91m' + line + '\033[0m') # Print red
            else:
                sys.stdout.write(line)

    ### Get the reference

    # Create the file name
    filename = self.get_file_name()

    # Add path to artemis references
    relative_path_file = os.path.dirname(__file__)
    relative_path_ref = relative_path_file[:-16] + '/artemis_references/'
    filepath = os.path.join(relative_path_ref, filename)

    assert os.path.isfile(filepath)
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
        dir_path = os.path.dirname(__file__) + '/outputs'
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