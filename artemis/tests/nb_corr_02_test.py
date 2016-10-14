from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet, set_scenario
import pytest

xfail = pytest.mark.xfail

@dataset([DataSet("nb-corr-02")])
class NbCorr02():
    """
    TODO: put there comments about the dataset
    """
    def test_nb_corr_02_01(self):
        self.journey(_from="stop_area:NC2:SA:1",
                     to="stop_area:NC2:SA:4", datetime="20041213T0700")


@set_scenario({"nb-corr-02": {"scenario": "default"}})
class TestNbCorr02Default(NbCorr02, ArtemisTestFixture):
    pass

@set_scenario({"nb-corr-02": {"scenario": "new_default"}})
class TestNbCorr02NewDefault(NbCorr02, ArtemisTestFixture):
    pass


@xfail(reason="Unsupported experimental scenario!", raises=AssertionError)
@set_scenario({"nb-corr-02": {"scenario": "experimental"}})
class TestNbCorr02Experimental(NbCorr02, ArtemisTestFixture):
    pass