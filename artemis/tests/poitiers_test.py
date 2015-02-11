from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet
import pytest
xfail = pytest.mark.xfail

@dataset([DataSet("poitiers")])
class TestPoitiers(ArtemisTestFixture):
    """
    """
    def test_poitiers_01(self):
        """
        ID artemis v1: 3
        """
        self.journey(_from="stop_area:POI:SA:10001",
                     to="stop_area:POI:SA:10046", datetime="20091117T070000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_poitiers_02(self):
        """
        ID artemis v1: 4
        """
        self.journey(_from="stop_area:POI:SA:10001",
                     to="stop_area:POI:SA:10046", datetime="20091116T235000",
                     walking_speed="0.83", max_duration_to_pt="1800")

    def test_poitiers_03(self):
        """
        ID artemis v1: 5
        """
        self.journey(_from="stop_area:POI:SA:10001",
                     to="stop_area:POI:SA:10046", datetime="20091116T225000",
                     walking_speed="0.83", max_duration_to_pt="1800")

    @xfail(reason="http://jira.canaltp.fr/browse/NAVITIAII-1575", raises=AssertionError)
    def test_poitiers_04(self):
        """
        ID artemis v1: 6
        """
        self.journey(_from="stop_area:POI:SA:10001",
                     to="stop_area:POI:SA:10046", datetime="20091116T002000",
                     walking_speed="0.83", max_duration_to_pt="1800")

    @xfail(reason="http://jira.canaltp.fr/browse/NAVITIAII-1575", raises=AssertionError)
    def test_poitiers_05(self):
        """
        ID artemis v1: 7
        """
        self.journey(_from="stop_area:POI:SA:10001",
                     to="stop_area:POI:SA:10046", datetime="20091117T002000",
                     walking_speed="0.83", max_duration_to_pt="1800")

    def test_poitiers_06(self):
        """
        ID artemis v1: 8
        """
        self.journey(_from="stop_area:POI:SA:10001",
                     to="stop_area:POI:SA:10046", datetime="20091114T002000",
                     walking_speed="0.83", max_duration_to_pt="1800")

    def test_poitiers_07(self):
        """
        ID artemis v1: 12
        """
        self.journey(_from="stop_area:POI:SA:10001",
                     to="stop_area:POI:SA:10114", datetime="20090906T070000",
                     walking_speed="0.83", max_duration_to_pt="240")

    @xfail(reason="http://jira.canaltp.fr/browse/NAVITIAII-1468", raises=AssertionError)
    def test_poitiers_08(self):
        """
        ID artemis v1: 13
        """
        self.journey(_from="stop_area:POI:SA:10001",
                     to="stop_area:POI:SA:10114", datetime="20091007T180000",
                     walking_speed="0.83", max_duration_to_pt="1200")
