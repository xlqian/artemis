"""
py test discover this file by default

Used to run some stuff at global scope
"""
import logging
import pytest
from artemis import utils
from artemis.configuration_manager import config
import requests
from retrying import retry
import ujson


def pytest_addoption(parser):
    """
    We add a pytest option to
    * skip the cities integration
    * skip the data integration (if it has been done before, it can save some time)
    """
    parser.addoption("--skip_cities", action="store_true", help="skip cities loading")
    parser.addoption("--skip_bina", action="store_true", help="skip binarization")
    parser.addoption("--hard_journey_check", action="store_true", help="journeys comparison is made on full response")
    parser.addoption("--check_ref", action="store_true",
                     help="only check that response is consistent with full response in reference files")
    parser.addoption("--create_ref", action="store_true", help="create a reference file using the response received - USE WITH CAUTION")


@pytest.fixture(scope="session", autouse=True)
def load_cities(request):
    """
    Load cities before running the tests
    """

    def get_last_cities_job():
        r = requests.get(config['URL_TYR'] + "/v0/cities/status")
        r.raise_for_status()
        return ujson.loads(r.text)['latest_job']

    # wait 5 min at most
    @retry(stop_max_delay=300000, wait_fixed=500)
    def wait_for_cities_completion():

        last_cities_job = get_last_cities_job()
        if last_cities_job and last_cities_job['state'] != 'done':
            raise Exception("Cities task still running...")

    log = logging.getLogger(__name__)
    if request.config.getvalue("skip_cities") or request.config.getvalue("check_ref"):
        log.info("skipping cities loading")
        return

    if config.get('USE_ARTEMIS_NG'):
        log.info('Posting cities')
        url = config['URL_TYR']+"/v0/cities/"
        files = {'file': open(config['CITIES_INPUT_FILE'], 'rb')}
        r = requests.post(url, files=files)
        r.raise_for_status()

        wait_for_cities_completion()
        log.info('Cities task finished')
        return

    log.info("loading cities database")

    utils.launch_exec('cities -i {input} --connection-string'
                      .format(input=config['CITIES_INPUT_FILE']),
                      additional_args=[config['CITIES_DB']])

    log.info("cities database loaded")
