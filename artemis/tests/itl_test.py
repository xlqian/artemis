from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet
import pytest
xfail = pytest.mark.xfail

@xfail(reason="http://jira.canaltp.fr/browse/NAVITIAII-1463", raises=AssertionError)
@dataset([DataSet("itl")])
class TestItl(ArtemisTestFixture):
    """
    test local traffic policy constraint
    """

    def test_itl_01(self):
        self.journey(_from="stop_area:ITL:SA:1",
                     to="stop_area:ITL:SA:7",
                     datetime="20041213T070000")

    def test_itl_02(self):
        self.journey(_from="stop_area:ITL:SA:1",
                     to="stop_area:ITL:SA:7",
                     datetime="20041213T070100")
