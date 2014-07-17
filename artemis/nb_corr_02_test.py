from artemis.test_mechanism import ArtemisTestFixture, dataset


@dataset(["nb-corr-02"])
class TestNbCorr02(ArtemisTestFixture):
    """
    TODO: put there comments about the dataset
    """
    def test_nb_corr_02_01(self):
        self.journey(_from="stop_area:NC2:SA:1",
                     to="stop_area:NC2:SA:4", datetime="20041213T0700")
