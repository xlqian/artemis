from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet


@dataset([DataSet("nb-corr-01")])
class TestNbCorr01(ArtemisTestFixture):
    """
    TODO: put there comments about the dataset
    """
    def test_nb_corr_01_01(self):
        self.journey(_from="stop_area:NC1:SA:1",
                     to="stop_area:NC1:SA:4", datetime="20041213T0700")
