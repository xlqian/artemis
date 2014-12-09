from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet


@dataset([DataSet("nb-corr-03")])
class TestNbCorr03(ArtemisTestFixture):
    """
    TODO: put there comments about the dataset
    """
    def test_nb_corr_03_01(self):
        self.journey(_from="stop_area:NC3:SA:1",
                     to="stop_area:NC3:SA:4", datetime="20041213T0700")

    def test_nb_corr_03_02(self):
        self.journey(_from="stop_area:NC3:SA:1",
                     to="stop_area:NC3:SA:5", datetime="20041213T0700")
