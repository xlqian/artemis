import requests
import inspect
import re
from flask import json
from artemis import default_checker, utils
import base_pytest2



# Beginning of the URL : we want the request to go to my own Jormun on my own machine
URL = 'http://127.0.0.1:9191/v1/coverage/default/journeys?'



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
    base_pytest2.compare_with_ref_louis(self, dict_resp)



class TestAuvergne(base_pytest2.TestFixture):


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