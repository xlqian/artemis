from utils import TestFixture, journey_test

class TestAuvergne(TestFixture):

    """
    test for new_default with data from auvergne
    """
    def test_auvergne_02(self):
        """
        http://jira.canaltp.fr/browse/NAVITIAII-2016
        """
       journey_test(_from="admin:fr:63135",
                    to="3.121833801269531;45.885276435738504", datetime="20160118T120300",
                    first_section_mode=['bike', 'bss', 'walking', 'car'],
                    last_section_mode=['walking'],
                    min_nb_journeys=3,
                    _night_bus_filter_base_factor=7200,
                    max_duration_to_pt=1800)
