from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet, set_scenario
import pytest
xfail = pytest.mark.xfail

@dataset([DataSet("itl")])
class Itl(object):
    """
    test local traffic policy constraint
    """

    @xfail(reason="http://jira.canaltp.fr/browse/NAVITIAII-1463", raises=AssertionError)
    def test_itl_01(self):
        self.journey(_from="stop_area:ITL:SA:1", to="stop_area:ITL:SA:7", datetime="20041213T070000")

    @xfail(reason="http://jira.canaltp.fr/browse/NAVITIAII-1584", raises=AssertionError)
    def test_itl_02(self):
        self.journey(_from="stop_area:ITL:SA:1",
                     to="stop_area:ITL:SA:7",
                     datetime="20041213T070100")


@set_scenario({"itl": {"scenario": "default"}})
class TestItlDefault(Itl, ArtemisTestFixture):
    pass

@set_scenario({"itl": {"scenario": "new_default"}})
class TestItlNewDefault(Itl, ArtemisTestFixture):
    pass


@set_scenario({"itl": {"scenario": "experimental"}})
class TestItlExperimental(Itl, ArtemisTestFixture):
    pass
