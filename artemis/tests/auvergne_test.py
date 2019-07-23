from artemis.test_mechanism import dataset, DataSet, set_scenario
from artemis.tests.fixture import ArtemisTestFixture
import pytest

xfail = pytest.mark.xfail

@dataset([DataSet("fr-auv")])
class Auvergne(object):
    """
    test for new_default with data from auvergne
    """
    def test_auvergne_01(self):
        """
        http://jira.canaltp.fr/browse/NAVITIAII-2020
        """
        self.journey(_from="poi:osm:node:303386067",
                     to="3.0630843999999797;45.7589254", datetime="20160121T170000",
                     first_section_mode=['bike', 'bss', 'walking', 'car'],
                     last_section_mode=['walking'],
                     min_nb_journeys=3,
                     max_duration_to_pt=1200)

    def test_auvergne_02(self):
        """
        http://jira.canaltp.fr/browse/NAVITIAII-2016
        """
        self.journey(_from="admin:fr:63135",
                     to="3.121833801269531;45.885276435738504", datetime="20160118T120300",
                     first_section_mode=['bike', 'bss', 'walking', 'car'],
                     last_section_mode=['walking'],
                     min_nb_journeys=3,
                     _night_bus_filter_base_factor=7200,
                     max_duration_to_pt=1800)

    def test_auvergne_03(self):
        """
        same that 02, but this time the nigth bus filter should remove walking solution since they are too late
        """
        self.journey(_from="admin:fr:63135",
                     to="3.121833801269531;45.885276435738504", datetime="20160118T120300",
                     first_section_mode=['bike', 'bss', 'walking', 'car'],
                     last_section_mode=['walking'],
                     min_nb_journeys=3,
                     _night_bus_filter_base_factor=3600,
                     max_duration_to_pt=1800)

    def test_auvergne_04(self):
        """
        http://jira.canaltp.fr/browse/NAVITIAII-2011
        """
        self.journey(_from="3.0902481079101562;45.8892912569653",
                     to="3.1218767166137695;45.88621444878203", datetime="20160118T120300",
                     first_section_mode=['bike', 'bss', 'walking', 'car'],
                     last_section_mode=['walking'],
                     min_nb_journeys=3)

    def test_min_nb_journeys(self):
        """
        https://jira.kisio.org/browse/NAVP-863
        """
        self.journey(_from="3.10763;45.78656",
                     to="3.04947;45.76422", datetime="20160120T100000",
                     min_nb_journeys=5)

    def test_no_shared_section(self):
        """
        https://jira.kisio.org/browse/NAVP-858
        """
        self.journey(_from="3.10763;45.78656",
                     to="3.04947;45.76422", datetime="20160120T100000",
                     min_nb_journeys=5,
                     _no_shared_section=True)

    def test_free_radius_from(self):
        """
        https://jira.kisio.org/browse/NAVP-820
        """
        self.journey(_from="3.10763;45.78656",
                     to="3.04947;45.76422", datetime="20160120T100000",
                     free_radius_from=400)

    def test_geo_status(self):
        """
        check geodata sources and volume
        """
        self.api('_geo_status')

    def test_auvergne_admin_to_station(self):
        """
        test the admin to station
        starts from a small town near Clermont-ferrand to the clermont's station

        The response should be the same for new_default and experimental

        We should be able to:
           * crow fly directly from the main Cebazat stations
           * have a direct path from the center of the town
        """
        self.journey(_from="admin:fr:63063",
                     to="stop_area:SNC:SA:SAOCE87734004", datetime="20160117T120000",
                     first_section_mode=['walking', 'car'],
                     last_section_mode=['walking'])

    def test_time_frame_duration(self):
        """
        Test parameter 'timeframe_duration'.

        Without the parameter, we only have 1 result.
        But when setting 'timeframe_duration=600', we want to have all the possible
        itinaries withing the next 10 minutes (10 min * 60 sec).
        """
        self.journey(_from="3.08643;45.75419",
                     to="3.09981;45.77871",
                     datetime="20160118T080000",
                     timeframe_duration="600")

    def test_time_frame_duration_with_max_nb_journey(self):
        """
        Test the combination of 'timeframe_duration' along with 'max_nb_journeys'.

        'timeframe_duration=600' returns 7 itinaries that we want to filter down
        to only 3 using 'max_nb_journeys'
        """
        self.journey(_from="3.08643;45.75419",
                     to="3.09981;45.77871",
                     datetime="20160118T080000",
                     timeframe_duration="600",
                     max_nb_journeys="3")



@set_scenario({"fr-auv": {"scenario": "new_default"}})
class TestAuvergneNewDefault(Auvergne, ArtemisTestFixture):
    pass


@set_scenario({"fr-auv": {"scenario": "experimental"}})
class TestAuvergneExperimental(Auvergne, ArtemisTestFixture):
    @xfail(reason="we need to update the marshaller and the references for taxi distances and durations", raises=AssertionError)
    def test_first_last_section_mode_taxi(self):
        self.journey(_from="3.10763;45.78656",
                     to="3.04947;45.76422", datetime="20160120T100000",
                     min_nb_journeys=5,
                     taxi_speed=5,
                     first_section_mode=['taxi'],
                     last_section_mode=['taxi'])

    def test_one_mode_combination_fails(self):
        """

        first_section_mode = ['bike', 'walking']
        last_section_mode = ['bike', 'walking']

        because of max_bike_duration_to_pt=120, the mode pair (bike, bike) will raise
        an exception in distributed, but the remaining modes are OK, the scenario distributed
        should still return the result

        :return:
        """
        first_section_mode = ['bike', 'walking']
        last_section_mode = ['bike', 'walking']

        self.journey(_from="3.11291;45.92753",
                     to="admin:fr:63300",
                     datetime="20160122T080000",
                     first_section_mode=first_section_mode,
                     last_section_mode=last_section_mode,
                     max_bike_duration_to_pt=120)
