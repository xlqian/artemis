from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet, set_scenario

@dataset([DataSet("prolong-mano")])
class ProlongMano(object):
    """
    TODO: put there comments about the dataset
    """
    def test_prolong_mano_01(self):
        self.journey(_from="stop_area:PRM:SA:1",
                     to="stop_area:PRM:SA:5", datetime="20041213T0700")

    def test_prolong_mano_02(self):
        self.journey(_from="stop_area:PRM:SA:1",
                     to="stop_area:PRM:SA:9", datetime="20041213T0700")

@set_scenario({"prolong-mano": {"scenario": "default"}})
class TestProlongManoDefault(ProlongMano, ArtemisTestFixture):
    pass

@set_scenario({"prolong-mano": {"scenario": "new_default"}})
class TestProlongManoNewDefault(ProlongMano, ArtemisTestFixture):
    pass


@set_scenario({"prolong-mano": {"scenario": "experimental"}})
class TestProlongManoExperimental(ProlongMano, ArtemisTestFixture):
    pass
