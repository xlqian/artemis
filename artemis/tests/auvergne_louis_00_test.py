import base_pytest

class TestAuvergne(base_pytest.TestFixture):


    """
    test for new_default with data from auvergne
    """
    def test_auvergne_01(self):
        """
        http://jira.canaltp.fr/browse/NAVITIAII-2020
        """

        # We shall just call the journey function here, the whole test is hidden inside.
        base_pytest.journey_Test(self, _from="poi:osm:node:303386067",
                           to="3.0630843999999797;45.7589254", datetime="20160121T170000",
                           first_section_mode=['bike', 'bss', 'walking', 'car'],
                           last_section_mode=['walking'],
                           min_nb_journeys=3,
                           max_duration_to_pt=1200)