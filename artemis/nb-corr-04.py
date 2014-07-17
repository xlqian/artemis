from artemis.test_mechanism import ArtemisTestFixture, dataset


@dataset(["nb-corr-04"])
class TestNbCorr04(ArtemisTestFixture):
    """
    TODO: put there comments about the dataset
    """
    def test_nb_corr_04_01(self):
        self.journey(_from="stop_area:NC4:SA:1",
                     to="stop_area:NC4:SA:4", datetime="20041213T0700")

    def test_nb_corr_04_02(self):
        self.journey(_from="stop_area:NC4:SA:1",
                     to="stop_area:NC4:SA:4", datetime="20041213T0700")
