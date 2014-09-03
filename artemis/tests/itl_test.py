from artemis.test_mechanism import ArtemisTestFixture, dataset


@dataset(["itl"])
class TestItl(ArtemisTestFixture):
    """
    TODO: put there comments about the dataset
    """

    def test_itl_01(self):
        self.journey(_from="stop_area:ITL:SA:1",
                     to="stop_area:ITL:SA:7",
                     datetime="20041213T070000")
