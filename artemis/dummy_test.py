import logging
import urllib2
from artemis.test_mechanism import ArtemisTestFixture


class TestDummyJourney(ArtemisTestFixture):

    def test_call_to_kraken(self):
        raw_response = urllib2.urlopen("http://localhost:5000/v1")

        response = raw_response.read()
        logging.getLogger(__name__).info("we got : {}".format(response))




