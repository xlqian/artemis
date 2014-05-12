"""
Lots of helper functions to ease tests
"""
import os
import urllib2
import logging
from flask import json
from artemis.configuration_manager import config

_api_main_root_point = 'http://localhost:5000/'

_api_current_root_point = _api_main_root_point + 'v1/'


def api(url):
    """
    default call to the api
    call http://endpoint/v1/{url}
    """
    raw_response = urllib2.urlopen(url)

    response = raw_response.read()
    logging.getLogger(__name__).debug("we got : {}".format(response))

    json_resp = json.loads(response)
    return json_resp


def get_ref(call_id):
    """
    get the associated reference for this API call
    the reference is stored in the REFERENCE_FILE_PATH directory with the same name as the call_id
    """
    assert os.path.exists(config['REFERENCE_FILE_PATH']), \
        "no reference directory found: {} does not exists".format(config['REFERENCE_FILE_PATH'])

    ref_filename = os.path.join(config['REFERENCE_FILE_PATH'], call_id)

    assert os.path.isfile(ref_filename), \
        "No reference available for query {}, we can't test anything".format(call_id)

    _file = open(ref_filename, 'r')

    #ref_enhanced_response = _file.read()
    dict_response = json.load(_file)

    return dict_response["response"]  #only the response object is important, the rest is for debug


def compare_with_ref(resp, call_id):
    """
    compare the answer to it's reference
    """
    ref = get_ref(call_id)

    logging.getLogger(__name__).info("ref: {}".format(ref))
    assert ref == resp







