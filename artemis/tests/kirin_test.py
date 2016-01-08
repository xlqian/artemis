# -*- coding: utf-8 -*-

from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet, utils
import pytest
import requests
import os
from retrying import retry
XML_HEADER = {'Content-Type': 'application/xml;charset=utf-8'}


def _get_ire_data(name):
    """
    return an IRE input as string
    the name must be the name of a file in tests/fixtures
    """
    _file = os.path.join(os.path.dirname(__file__), 'fixtures', name)
    with open(_file, "r") as ire:
        return ire.read()


@dataset([DataSet("sncf")])
class TestRealTime(ArtemisTestFixture):
    """
    test RealTime on SNCF
    """

    def test_normal_train(self):
        self.journey(_from="stop_area:OCE:SA:87686006",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20151215T1420",
                     data_freshness="base_schedule")

    def test_cancel_train(self):
        response, _ = utils.api("coverage/sncf/status")
        last_rt_data_loaded = response['status']['last_rt_data_loaded']

        # TGV
        r = requests.post('http://kirin:9090/ire',
                          data=_get_ire_data('trip_removal_tgv_2913.xml'),
                          headers=XML_HEADER)
        # iDTGV
        r = requests.post('http://kirin:9090/ire',
                          data=_get_ire_data('trip_removal_tgv_6154.xml'),
                          headers=XML_HEADER)

        @retry(wait_fixed=2000)
        def wait_for_rt_reload():
            _response, _ = utils.api("coverage/sncf/status")
            if last_rt_data_loaded == _response['status']['last_rt_data_loaded']:
                raise Exception("not loaded")
            return
        wait_for_rt_reload()

        self.journey(_from="stop_area:OCE:SA:87686006",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20151215T1420",
                     data_freshness="realtime")

@dataset([DataSet("sncf")])
class TestRealTimeReload(ArtemisTestFixture):
    """
    Test kirin's real time reload, this test is run after TestRealTime,
    so previous disruptions should be reloaded in this test
    """

    def test_cancel_train(self):

        self.journey(_from="stop_area:OCE:SA:87686006",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20151215T1420",
                     data_freshness="realtime")