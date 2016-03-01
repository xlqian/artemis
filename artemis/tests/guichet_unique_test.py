
from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet, \
    send_ire, get_last_rt_loaded_time, wait_for_rt_reload
from artemis.default_checker import default_disruption_checker

COVERAGE = "guichet-unique"
@dataset([DataSet(COVERAGE)])
class TestGuichetUnique(ArtemisTestFixture):
    """
    """
    def test_guichet_unique_caen_to_marseille(self):
        """
        ID artemis v1: 0
        """
        self.journey(_from="admin:149197extern",
                     to="admin:76469extern", datetime="20120924T070000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_paris_to_rouen(self):
        """
        ID artemis v1: 1
        """
        self.journey(_from="admin:7444extern",
                     to="admin:75628extern", datetime="20121012T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_caen_to_brest(self):
        """
        ID artemis v1: 2
        """
        self.journey(_from="admin:149197extern",
                     to="admin:1076124extern", datetime="20121022T054500",
                     walking_speed="0.83", max_duration_to_pt="240", count="7", type="rapid")

    def test_guichet_unique_reims_to_paris(self):
        """
        ID artemis v1: 18
        """
        self.journey(_from="admin:36458extern",
                     to="admin:7444extern", datetime="20121020T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_avignon_to_marseille(self):
        """
        ID artemis v1: 19
        """
        self.journey(_from="admin:102478extern",
                     to="admin:76469extern", datetime="20120928T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_paris_to_avignon(self):
        """
        ID artemis v1: 20
        """
        self.journey(_from="admin:7444extern",
                     to="admin:102478extern", datetime="20121121T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_paris_to_ay(self):
        """
        ID artemis v1: 21
        """
        self.journey(_from="admin:7444extern",
                     to="admin:417494extern", datetime="20121121T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_paris_to_Avenay_Val_d_Or(self):
        """
        ID artemis v1: 22
        """
        self.journey(_from="admin:7444extern",
                     to="admin:2651291extern", datetime="20121025T120000",
                     walking_speed="0.83", max_duration_to_pt="6000")



    """
    test RealTime on SNCF
    """

    def test_no_disruption(self):
        """
        Request on disruptions before applying any
        We shouldn't have any
        """
        self.api('disruptions')

    def test_kirin_normal_train(self):
        """
        Requested departure: 2012/12/15 16:30
        From: Gare de Lyon, Paris
        To: Saint Charles, Marseille

        we should find a train travelling from 16:37 to 19:50
        """
        self.journey(_from="stop_area:OCE:SA:87686006",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20121215T1630",
                     data_freshness="realtime")

    def test_kirin_cancel_train(self):
        """
        test cancellation of the train

        Requested departure: 2012/12/15 16:30
        From: Gare de Lyon, Paris
        To: Saint Charles, Marseille

        Before the cancellation, we should find a train travelling from 16:37 to 19:50
        After the cancellation, a train travelling from 17:07 to 20:24 will be found
        """
        last_rt_data_loaded = get_last_rt_loaded_time(COVERAGE)

        # TGV
        send_ire('trip_removal_tgv_6121.xml')

        wait_for_rt_reload(last_rt_data_loaded, COVERAGE)

        # test that it is still OK in base-schedule
        self.journey(_from="stop_area:OCE:SA:87686006",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20121215T1630",
                     data_freshness="base_schedule")

        # test that RT is disrupted
        self.journey(_from="stop_area:OCE:SA:87686006",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20121215T1630",
                     data_freshness="realtime")

        self.api('vehicle_journeys/vehicle_journey:OCETGV-87686006-87751008-7:34580/disruptions',
                 response_checker=default_disruption_checker)

    def test_kirin_repeat_the_same_ire_and_reload_from_scratch(self):
        """
        test cancellation of the train

        Requested departure: 2012/12/20 17:00
        From: Gare de Lyon, Paris
        To: Saint Charles, Marseille

        After the cancellation, a train travelling from 18:19 to 21:29 should be found
        """
        last_rt_data_loaded = get_last_rt_loaded_time(COVERAGE)

        for i in range(5):
            send_ire('trip_removal_tgv_6123.xml')

        wait_for_rt_reload(last_rt_data_loaded, COVERAGE)

        self.journey(_from="stop_area:OCE:SA:87686006",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20121220T1700",
                     data_freshness="realtime")

        """
        At this point, an IRE is saved into the db,
        now we'll test the case where kraken is run from scratch and the previous
        IRE should be taken into account
        """
        last_rt_data_loaded = get_last_rt_loaded_time(COVERAGE)

        self.kill_the_krakens()
        self.pop_krakens()

        wait_for_rt_reload(last_rt_data_loaded, COVERAGE)

        self.journey(_from="stop_area:OCE:SA:87686006",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20121220T1700",
                     data_freshness="realtime")
