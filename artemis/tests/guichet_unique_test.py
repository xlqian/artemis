
from artemis.test_mechanism import dataset, DataSet, set_scenario
from artemis.tests.fixture import ArtemisTestFixture
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
        self.journey(_from="admin:fr:14118",
                     to="admin:fr:13055", datetime="20120924T070000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_paris_to_rouen(self):
        """
        ID artemis v1: 1
        """
        self.journey(_from="admin:fr:75056",
                     to="admin:fr:76540", datetime="20121012T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_caen_to_brest(self):
        """
        ID artemis v1: 2
        """
        self.journey(_from="admin:fr:14118",
                     to="admin:fr:29019", datetime="20121022T054500",
                     walking_speed="0.83", max_duration_to_pt="240", count="7", type="rapid")

    def test_guichet_unique_reims_to_paris(self):
        """
        ID artemis v1: 18
        """
        self.journey(_from="admin:fr:51454",
                     to="admin:fr:75056", datetime="20121020T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_avignon_to_marseille(self):
        """
        ID artemis v1: 19
        """
        self.journey(_from="admin:fr:84007",
                     to="admin:fr:13055", datetime="20120928T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_paris_to_avignon(self):
        """
        ID artemis v1: 20
        """
        self.journey(_from="admin:fr:75056",
                     to="admin:fr:84007", datetime="20121121T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_paris_to_ay(self):
        """
        ID artemis v1: 21
        """
        self.journey(_from="admin:fr:75056",
                     to="admin:fr:51030", datetime="20121121T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_paris_to_Avenay_Val_d_Or(self):
        """
        ID artemis v1: 22
        """
        self.journey(_from="admin:fr:75056",
                     to="admin:fr:51028", datetime="20121025T120000",
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
    test RealTime on SNCF (COTS)
    """
    def test_kirin_cots_trip_delay(self):
        """
        Test delay on a train

        Requested departure: 2012/11/20 16:00:00
        From: gare de Strasbourg (Strasbourg)
        To: gare de Marseille-St-Charles (Marseille)

        Before the delay, the train travels from 16:12:00 to 21:46:00
        After the delay, the train travels from 16:12:00 to 22:16:00
        """
        last_rt_data_loaded = self.get_last_rt_loaded_time(COVERAGE)
        self.send_cots('trip_delay_9580_tgv.json')
        self.wait_for_rt_reload(last_rt_data_loaded, COVERAGE)

        self.journey(_from="stop_area:OCE:SA:87212027",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20121120T160000",
                     data_freshness="realtime")

        self.journey(_from="stop_area:OCE:SA:87212027",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20121120T160000",
                     data_freshness="base_schedule")

    def test_kirin_cots_trip_removal(self):
        """
        Test removal of a train

        Requested departure: 2012/12/16 17:30:00
        From: gare de Bordeaux-St-Jean (Bordeaux)
        To: gare de Marseille-St-Charles (Marseille)

        Before the removal, a train (headsign: 4669) travels on 2012/12/16 from 17:31:00 to 23:46:00
        After the removal, an other train (headsign: 4655) travels on 2012/12/17 from 06:45:00 to 12:59:00
        """
        last_rt_data_loaded = self.get_last_rt_loaded_time(COVERAGE)
        self.send_cots('trip_removal_4669_ic.json')
        self.wait_for_rt_reload(last_rt_data_loaded, COVERAGE)  

        self.journey(_from="stop_area:OCE:SA:87581009",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20121216T173000",
                     data_freshness="realtime")

        self.journey(_from="stop_area:OCE:SA:87581009",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20121216T173000",
                     data_freshness="base_schedule")

    def test_kirin_cots_trip_deleted_partially(self):
        """
        Test removal of some stops of a vj

        Requested departure: 2012/11/19 12:36:00
        From: gare de Avignon-TGV (Avignon)
        To: gare de Marseille-St-Charles (Marseille)

        Before the removal of the stops, a train (headsign: 5312/5358) travels from 12:39:00 to 13:14:00
        After the removal of the departure stop, an other train (headsign: 5101) travels from 13:11:00 to 13:48:00
        """
        last_rt_data_loaded = self.get_last_rt_loaded_time(COVERAGE)
        self.send_cots('trip_partially_deleted_5312_tgv.json')
        self.wait_for_rt_reload(last_rt_data_loaded, COVERAGE)
        last_rt_data_loaded = self.get_last_rt_loaded_time(COVERAGE)
        self.send_cots('trip_partially_deleted_5358_tgv.json')
        self.wait_for_rt_reload(last_rt_data_loaded, COVERAGE)  

        self.journey(_from="stop_area:OCE:SA:87318964",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20121119T123600",
                     data_freshness="realtime")

        self.journey(_from="stop_area:OCE:SA:87318964",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20121119T123000",
                     data_freshness="base_schedule")   

    def test_kirin_cots_trip_observed_delay_passe_minuit(self):
        """
        Test delay of a train which arrival is the day after the departure

        Requested departure: 2012/12/16 22:30:00
        From: gare de Paris-Nord (Paris)
        To: gare de St Quentin (Saint-Quentin)

        Before the delay, the train travels from 2012/12/16 22:37:00 to 2012/12/17 00:16:00
        After the delay, the train travels from 2012/12/16 22:37:00 to 2012/12/17 00:41:00
        """
        last_rt_data_loaded = self.get_last_rt_loaded_time(COVERAGE)
        self.send_cots('trip_observed_delay_passe_minuit_847919_ter.json')
        self.wait_for_rt_reload(last_rt_data_loaded, COVERAGE)  

        self.journey(_from="stop_area:OCE:SA:87271007",
                     to="stop_area:OCE:SA:87296004",
                     datetime="20121216T223000",
                     data_freshness="realtime")

        self.journey(_from="stop_area:OCE:SA:87271007",
                     to="stop_area:OCE:SA:87296004",
                     datetime="20121216T223000",
                     data_freshness="base_schedule") 

    def test_kirin_cots_trip_departure_delayed_pass_midnight(self):
        """
        Test delay of a train with a departure without delay before midnight,
        then a departure after midnight with the delay

        Requested departure: 2012/12/16 23:40:00
        From: gare de Noyon (Noyon)
        To: gare de St Quentin (Saint-Quentin)

        Before the delay, the train travels from 2012/12/16 23:44:00 to 2012/12/17 00:16:00
        After the delay, the train travels from 2012/12/17 00:09:00 to 2012/12/17 00:41:00
        """
        last_rt_data_loaded = self.get_last_rt_loaded_time(COVERAGE)
        self.send_cots('trip_observed_delay_passe_minuit_847919_ter.json')
        self.wait_for_rt_reload(last_rt_data_loaded, COVERAGE)

        self.journey(_from="stop_area:OCE:SA:87276782",
                     to="stop_area:OCE:SA:87296004",
                     datetime="20121216T234000",
                     data_freshness="realtime")

        self.journey(_from="stop_area:OCE:SA:87276782",
                     to="stop_area:OCE:SA:87296004",
                     datetime="20121216T234000",
                     data_freshness="base_schedule")

    def test_kirin_cots_reload_from_scratch(self):
        """
        Test removal of a train

        Requested departure: 2012/12/16 17:30:00
        From: gare de Bordeaux-St-Jean (Bordeaux)
        To: gare de Marseille-St-Charles (Marseille)

        Before the removal, a train (headsign: 4669) travels on 2012/12/16 from 17:31:00 to 23:46:00
        After the removal, an other train (headsign: 4655) travels on 2012/12/17 from 06:45:00 to 12:59:00
        """
        last_rt_data_loaded = self.get_last_rt_loaded_time(COVERAGE)
        self.send_cots('trip_delay_9580_tgv.json')
        self.wait_for_rt_reload(last_rt_data_loaded, COVERAGE)

        self.journey(_from="stop_area:OCE:SA:87212027",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20121120T160000",
                     data_freshness="realtime")

        """
        At this point, the COTS feed is saved into the db,
        now the kraken is run from scratch and the previous COTS feed should be taken into account
        """
        last_rt_data_loaded = self.get_last_rt_loaded_time(COVERAGE)

        self.kill_the_krakens()
        self.pop_krakens()

        self.wait_for_rt_reload(last_rt_data_loaded, COVERAGE)

        self.journey(_from="stop_area:OCE:SA:87212027",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20121120T160000",
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
