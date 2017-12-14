"""
py test discover this file by default

Used to run some stuff at global scope
"""
import logging
import pytest
from artemis import utils
from artemis.configuration_manager import config


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


@pytest.fixture(scope="session", autouse=True)
def load_cities(request):
    """
    Before running the tests we want to load cities
    """
    log = logging.getLogger(__name__)
    if request.config.getvalue("skip_cities") or request.config.getvalue("check_ref"):
        log.info("skiping cities loading")
        return

    log.info("loading cities database")

    utils.launch_exec('cities -i {input} --connection-string'
                      .format(input=config['CITIES_INPUT_FILE']),
                      additional_args=[config['CITIES_DB']])

    log.info("cities database loaded")
