from artemis.test_mechanism import ArtemisTestFixture, dataset


@dataset(["corr-02"])
class TestCorr02(ArtemisTestFixture):
    """
    TODO: put there comments about the dataset
    """

    def test_corr_02_01(self):
        self.journey(_from="stop_area:CR2:SA:12",
                     to="stop_area:CR2:SA:4", datetime="20041213T0700")
