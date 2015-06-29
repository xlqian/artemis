from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet


@dataset([DataSet("corr-01")])
class TestCorr01(ArtemisTestFixture):
    """
    """

    def test_corr_01_01(self):
        """
        no solution found for this journey because number of transfers > 10
        """
        self.journey(_from="stop_area:CR1:SA:1",
                     to="stop_area:CR1:SA:13", datetime="20041210T0700", max_duration_to_pt=0)

    def test_corr_01_02(self):
        self.journey(_from="stop_area:CR1:SA:1",
                     to="stop_area:CR1:SA:13", datetime="20041210T0700", max_nb_transfers=11,
                     max_duration_to_pt=0)
