from artemis.test_mechanism import ArtemisTestFixture, dataset

#TODO: rename the test

@dataset(["boucle-01"])
class TestBoucle(ArtemisTestFixture):
    """
    TODO: put there comments about the dataset
    """

    def test_boucle_01(self):
        self.journey(_from="stop_area:BC1:SA:1",
                     to="stop_area:BC1:SA:6", datetime="20041213T0730")

    def test_boucle_02(self):
        self.journey(_from="stop_area:BC1:SA:3",
                     to="stop_area:BC1:SA:7", datetime="20041213T0730")

    def test_boucle_03(self):
        self.journey(_from="stop_area:BC1:SA:8",
                     to="stop_area:BC1:SA:5", datetime="20041213T0730")
