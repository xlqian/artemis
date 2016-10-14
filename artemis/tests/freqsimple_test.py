from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet, set_scenario
import pytest
xfail = pytest.mark.xfail

@dataset([DataSet("freqsimple")])
class FreqSimple():
    """
    TODO: put there comments about the dataset
    """
    def test_freqsimple_01(self):
        self.journey(_from="stop_area:FQS:SA:GRA",
                     to="stop_area:FQS:SA:MBC", datetime="20070417T0540")

    def test_freqsimple_02(self):
        self.journey(_from="stop_area:FQS:SA:GRA",
                     to="stop_area:FQS:SA:MBC", datetime="20070417T0500")

    def test_freqsimple_03(self):
        self.journey(_from="stop_area:FQS:SA:MBC",
                     to="stop_area:FQS:SA:GRA", datetime="20070417T0100")

    def test_freqsimple_04(self):
        self.journey(_from="stop_area:FQS:SA:MBC",
                     to="stop_area:FQS:SA:GRA", datetime="20070417T0520", datetime_represents="arrival")

    def test_freqsimple_05(self):
        self.journey(_from="stop_area:FQS:SA:MBC",
                     to="stop_area:FQS:SA:GRA", datetime="20070417T0550", datetime_represents="arrival")


@set_scenario({"freqsimple": {"scenario": "default"}})
class TestFreqSimpleDefault(FreqSimple, ArtemisTestFixture):
    pass

@set_scenario({"freqsimple": {"scenario": "new_default"}})
class TestFreqSimpleNewDefault(FreqSimple, ArtemisTestFixture):
    pass


@xfail(reason="Unsupported experimental scenario!", raises=AssertionError)
@set_scenario({"freqsimple": {"scenario": "experimental"}})
class TestFreqSimpleExperimental(FreqSimple, ArtemisTestFixture):
    pass