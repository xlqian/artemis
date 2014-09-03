from artemis.test_mechanism import ArtemisTestFixture, dataset


@dataset(["freqgtfs"])
class TestFreqGtfs(ArtemisTestFixture):
    """
    test frequencies to stops serialisation by FUSiO
    """

    def test_freqgtfs_01(self):
        self.journey(_from="stop_area:FQG:SA:35",
                     to="stop_area:FQG:SA:1",
                     datetime="20070417T054000")