# -*- coding: utf-8 -*-

from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet, utils, send_ire, wait_for_rt_reload


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
        send_ire('trip_removal_tgv_2913.xml')
        # iDTGV
        send_ire('trip_removal_tgv_6154.xml')

        wait_for_rt_reload(last_rt_data_loaded)

        self.journey(_from="stop_area:OCE:SA:87686006",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20151215T1420",
                     data_freshness="realtime")

    def test_repeat_the_same_ire(self):
        response, _ = utils.api("coverage/sncf/status")
        last_rt_data_loaded = response['status']['last_rt_data_loaded']

        for i in range(5):
            send_ire('trip_removal_tgv_6123.xml')
            send_ire('trip_removal_tgv_6123.xml')
            send_ire('trip_removal_tgv_6123.xml')
            send_ire('trip_removal_tgv_6123.xml')

        wait_for_rt_reload(last_rt_data_loaded)

        self.journey(_from="stop_area:OCE:SA:87686006",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20151220T1700",
                     data_freshness="realtime")

    def test_reload_from_scratch(self):

        response, _ = utils.api("coverage/sncf/status")
        last_rt_data_loaded = response['status']['last_rt_data_loaded']

        self.kill_the_krakens()
        self.pop_krakens()

        wait_for_rt_reload(last_rt_data_loaded)

        self.journey(_from="stop_area:OCE:SA:87686006",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20151215T1420",
                     data_freshness="realtime")
