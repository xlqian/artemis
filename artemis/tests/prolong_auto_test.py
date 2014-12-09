from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet


@dataset([DataSet("prolong-auto")])
class TestProlongAuto(ArtemisTestFixture):
    """
    TODO: put there comments about the dataset
    """
    def test_prolong_auto_01(self):
        self.journey(_from="stop_area:PRA:SA:1",
                     to="stop_area:PRA:SA:5", datetime="20041213T0700")

    def test_prolong_auto_02(self):
        self.journey(_from="stop_area:PRA:SA:1",
                     to="stop_area:PRA:SA:9", datetime="20041213T0700")

    def test_prolong_auto_03(self):
        self.journey(_from="stop_area:PRA:SA:1",
                     to="stop_area:PRA:SA:5", datetime="20041213T0700")
