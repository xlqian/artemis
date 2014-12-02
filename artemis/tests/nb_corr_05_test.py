from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet


@dataset([DataSet("nb-corr-05")])
class TestNbCorr05(ArtemisTestFixture):
    """
    TODO: put there comments about the dataset
    """
    def test_nb_corr_05_01(self):
        self.journey(_from="stop_area:NC5:SA:1",
                     to="stop_area:NC5:SA:4", datetime="20041213T0700")
