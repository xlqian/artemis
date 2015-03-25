from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet
import pytest
xfail = pytest.mark.xfail

@dataset([DataSet("freqparis")])
class TestFreqParis(ArtemisTestFixture):
    """
    TODO: put there comments about the dataset
    """
    @xfail(reason="http://jira.canaltp.fr/browse/NAVITIAII-1459", raises=AssertionError)
    def test_freqparis_01(self):
        self.journey(_from="stop_area:FQP:SA:defen",
                     to="stop_area:FQP:SA:grest", datetime="20090922T0700")

    def test_freqparis_02(self):
        self.journey(_from="stop_area:FQP:SA:defen",
                     to="stop_area:FQP:SA:grest", datetime="20090922T2330")

    def test_freqparis_03(self):
        self.journey(_from="stop_area:FQP:SA:defen",
                     to="stop_area:FQP:SA:grest", datetime="20090922T2200")

    @xfail(reason="http://jira.canaltp.fr/browse/NAVITIAII-1579", raises=AssertionError)
    def test_freqparis_04(self):
        self.journey(_from="stop_area:FQP:SA:defen",
                     to="stop_area:FQP:SA:grest", datetime="20090922T0008", datetime_represents="arrival")

    @xfail(reason="http://jira.canaltp.fr/browse/NAVITIAII-1580", raises=AssertionError)
    def test_freqparis_05(self):
        self.journey(_from="stop_area:FQP:SA:defen",
                     to="stop_area:FQP:SA:grest", datetime="20090922T0020", datetime_represents="arrival")

    def test_freqparis_06(self):
        self.journey(_from="stop_area:FQP:SA:defen",
                     to="stop_area:FQP:SA:grest", datetime="20090922T2350")

    def test_freqparis_07(self):
        self.journey(_from="stop_area:FQP:SA:defen",
                     to="stop_area:FQP:SA:grest", datetime="20090922T2355")
