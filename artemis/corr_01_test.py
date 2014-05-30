from artemis.test_mechanism import ArtemisTestFixture, dataset


@dataset(["corr-01"])
class TestBoucle(ArtemisTestFixture):
    """
    TODO: put there comments about the dataset
    """

    def test_boucle_01(self):
        self.journey(_from="stop_area:CR1:SA:1",
                     to="stop_area:CR1:SA:13", datetime="20041210T0700")
