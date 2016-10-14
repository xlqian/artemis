from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet, set_scenario
import pytest

xfail = pytest.mark.xfail

@dataset([DataSet("nb-corr-03")])
class NbCorr03():
    """
    TODO: put there comments about the dataset
    """
    def test_nb_corr_03_01(self):
        self.journey(_from="stop_area:NC3:SA:1",
                     to="stop_area:NC3:SA:4", datetime="20041213T0700")

    def test_nb_corr_03_02(self):
        self.journey(_from="stop_area:NC3:SA:1",
                     to="stop_area:NC3:SA:5", datetime="20041213T0700")


@set_scenario({"nb-corr-03": {"scenario": "default"}})
class TestNbCorr03Default(NbCorr03, ArtemisTestFixture):
    pass

@set_scenario({"nb-corr-03": {"scenario": "new_default"}})
class TestNbCorr03NewDefault(NbCorr03, ArtemisTestFixture):
    pass


@xfail(reason="Unsupported experimental scenario!", raises=AssertionError)
@set_scenario({"nb-corr-03": {"scenario": "experimental"}})
class TestNbCorr03Experimental(NbCorr03, ArtemisTestFixture):
    pass