import requests
import inspect
import re
from flask import json
from artemis import default_checker
import os


# Beginning of the URL : we want the request to go to my own Jormun on my own machine
URL = 'http://127.0.0.1:9191/v1/coverage/default/journeys?'

# Path to my artemis references
PATH_REF = '/home/louis_gaillet/Projets/Artemis/artemis_references/'

# regexp used to identify a test method (simplified version of nose)
_test_method_regexp = re.compile("^(test_.*|.*_test)$")



def journey_Test(self, _from, to, datetime,
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
    query = URL + query

    # Get the json answer of the request (it is just a string here)
    raw_response = requests.get(query)

    # Transform the string into a dictionary
    dict_resp = json.loads(raw_response.text)

    # Comparing my response and my reference
    compare_with_ref(self, dict_resp)


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


def compare_with_ref(self, response,
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



#----------------------------------------------------------------------------------------------
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



class TestAuvergne(TestFixture):


    """
    test for new_default with data from auvergne
    """
    def test_auvergne_01(self):
        """
        http://jira.canaltp.fr/browse/NAVITIAII-2020
        """

        # We shall just call the journey function here, the whole test is hidden inside.
        journey_Test(self, _from="poi:osm:node:303386067",
                           to="3.0630843999999797;45.7589254", datetime="20160121T170000",
                           first_section_mode=['bike', 'bss', 'walking', 'car'],
                           last_section_mode=['walking'],
                           min_nb_journeys=3,
                           max_duration_to_pt=1200)