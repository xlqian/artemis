import inspect
from artemis import default_checker, utils
import os
from flask import json

# Path to my artemis references
PATH_REF = '/home/louis_gaillet/Projets/Artemis/artemis_references/'

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



def compare_with_ref_louis(self, response,
                        response_checker=default_checker.default_journey_checker):
    """
    This function take the response (which is a dictionary) and compare it to a the reference
    It first goes finding the reference
    Then filters both ref and resp
    Finaly it compares them

    """

    ### Get the reference

    # Create the file name
    filename = self.get_file_name()

    # Add path to artemis references
    # config = flask_conf.Config(os.path.dirname(os.path.realpath(__file__)))
    filepath = os.path.join(PATH_REF, filename)

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


    """
    # This part is only to check ref and resp content
    with open('reference.txt', 'w') as reference_text:
        reference_text.write(json.dumps(filtered_reference, indent=4))

    with open('response.txt', 'w') as response_text:
        response_text.write(json.dumps(filtered_response, indent=4))
    """


    ### Compare answer and reference
    response_checker.compare(filtered_response, filtered_reference)