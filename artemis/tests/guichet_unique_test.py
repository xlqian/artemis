
from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet, \
    send_ire, get_last_rt_loaded_time, wait_for_rt_reload, set_scenario
import pytest

xfail = pytest.mark.xfail

COVERAGE = "guichet-unique"
@dataset([DataSet(COVERAGE)])
class GuichetUnique(object):
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

    def test_too_long_waiting_filter(self):
        """
        Test a journey from saint quentin -> saint just in the new_default scenario

        The query is late, and without filter we have 2 journeys

        * One where the traveller leaves at 20h19, sleeps at Amiens and arrive in the morning (6h22)
        * One where the traveller leaves at 7h22 and arrive at 9h14

        We don't want the first journey, so it is filtered and we should only have the second one

        linked to http://jira.canaltp.fr/browse/NAVITIAII-2000
        """
        self.journey(_from="stop_area:OCE:SA:87296004",
                     to="stop_area:OCE:SA:87313270", datetime="20121123T2019",
                     _override_scenario="new_default")

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

        self.api('vehicle_journeys/vehicle_journey:OCE:SN006121F02003/disruptions')

        # test of departures with a cancelled train
        # in realtime we should have 6 passages, and in base_schedule we should have 7
        # the addditional passage should be the one at 20121215T163700
        self.api('stop_areas/stop_area:OCE:SA:87686006/'
                 'lines/line:OCE:TGV-87751008-87686006/departures?from_datetime=20121215T1630')

        self.api('stop_areas/stop_area:OCE:SA:87686006/'
                 'lines/line:OCE:TGV-87751008-87686006/departures'
                 '?from_datetime=20121215T1630&data_freshness=base_schedule')

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


@set_scenario({COVERAGE: {"scenario": "default"}})
class TestGuichetUniqueDefault(GuichetUnique, ArtemisTestFixture):
    pass

@set_scenario({COVERAGE: {"scenario": "new_default"}})
class TestGuichetUniqueNewDefault(GuichetUnique, ArtemisTestFixture):
    @xfail(reason="Unsupported new_default scenario!", raises=AssertionError)
    def test_guichet_unique_caen_to_marseille(self):
        super(TestGuichetUniqueNewDefault, self).test_guichet_unique_caen_to_marseille()


@set_scenario({COVERAGE: {"scenario": "experimental"}})
class TestGuichetUniqueExperimental(GuichetUnique, ArtemisTestFixture):
    @xfail(reason="Unsupported experimental scenario!", raises=AssertionError)
    def test_guichet_unique_caen_to_marseille(self):
        super(TestGuichetUniqueExperimental, self).test_guichet_unique_caen_to_marseille()
    @xfail(reason="Unsupported experimental scenario!", raises=AssertionError)
    def test_guichet_unique_paris_to_rouen(self):
        super(TestGuichetUniqueExperimental, self).test_guichet_unique_paris_to_rouen()
    @xfail(reason="Unsupported experimental scenario!", raises=AssertionError)
    def test_guichet_unique_caen_to_brest(self):
        super(TestGuichetUniqueExperimental, self).test_guichet_unique_caen_to_brest()
    @xfail(reason="Unsupported experimental scenario!", raises=AssertionError)
    def test_guichet_unique_reims_to_paris(self):
        super(TestGuichetUniqueExperimental, self).test_guichet_unique_reims_to_paris()
    @xfail(reason="Unsupported experimental scenario!", raises=AssertionError)
    def test_guichet_unique_avignon_to_marseille(self):
        super(TestGuichetUniqueExperimental, self).test_guichet_unique_avignon_to_marseille()
    @xfail(reason="Unsupported experimental scenario!", raises=AssertionError)
    def test_guichet_unique_paris_to_avignon(self):
        super(TestGuichetUniqueExperimental, self).test_guichet_unique_paris_to_avignon()
    @xfail(reason="Unsupported experimental scenario!", raises=AssertionError)
    def test_guichet_unique_paris_to_ay(self):
        super(TestGuichetUniqueExperimental, self).test_guichet_unique_paris_to_ay()
    @xfail(reason="Unsupported experimental scenario!", raises=AssertionError)
    def test_guichet_unique_paris_to_Avenay_Val_d_Or(self):
        super(TestGuichetUniqueExperimental, self).test_guichet_unique_paris_to_Avenay_Val_d_Or()
