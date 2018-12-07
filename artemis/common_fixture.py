import logging
import artemis.utils as utils
import requests
from artemis.configuration_manager import config

logger = logging.getLogger(__name__)


class CommonTestFixture(object):
    def send_cots(self, cots_file_name):
        r = requests.post(config['KIRIN_API'] + '/cots',
                          data=utils.get_rt_data(cots_file_name).encode('UTF-8'),
                          headers={'Content-Type': 'application/json;charset=utf-8'})
        r.raise_for_status()

