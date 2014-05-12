"""
Lots of helper functions to ease tests
"""
import urllib2
import logging

_api_main_root_point = 'http://localhost:5000/'

_api_current_root_point = _api_main_root_point + 'v1/'


def api(url):
    """
    default call to the api
    call http://endpoint/v1/url

    compare the answer to it's reference
    """
    raw_response = urllib2.urlopen(_api_current_root_point + url)

    response = raw_response.read()
    logging.getLogger(__name__).debug("we got : {}".format(response))
    return response






