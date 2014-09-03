from artemis.test_mechanism import ArtemisTestFixture, dataset


@dataset(["test-03"])
class TestTest03(ArtemisTestFixture):
    """
    TODO: put there comments about the dataset
    """
    def test_test_03_01(self):
        self.journey(_from="stop_area:TS3:SA:1",
                     to="stop_area:TS3:SA:6", datetime="20041214T0700")

