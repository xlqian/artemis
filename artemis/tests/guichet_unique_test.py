from artemis.test_mechanism import ArtemisTestFixture, dataset


@dataset(["guichet-unique"])
class TestGuichetUnique(ArtemisTestFixture):
    """
    """
    def test_guichet_unique_caen_to_marseille(self):
        """
        ID artemis v1: 0
        """
        self.journey(_from="admin:14118",
                     to="admin:13055", datetime="20120924T070000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_paris_to_rouen(self):
        """
        ID artemis v1: 1
        """
        self.journey(_from="admin:75056",
                     to="admin:76540", datetime="20121012T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_caen_to_brest(self):
        """
        ID artemis v1: 2
        """
        self.journey(_from="admin:14118",
                     to="admin:75056", datetime="20121022T054500",
                     walking_speed="0.83", max_duration_to_pt="240", count="7", type="rapid")

    def test_guichet_unique_reims_to_paris(self):
        """
        ID artemis v1: 18
        """
        self.journey(_from="admin:51454",
                     to="admin:75056", datetime="20121020T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_avignon_to_marseille(self):
        """
        ID artemis v1: 19
        """
        self.journey(_from="admin:84007",
                     to="admin:13055", datetime="20120928T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_paris_to_avignon(self):
        """
        ID artemis v1: 20
        """
        self.journey(_from="admin:75056",
                     to="admin:84007", datetime="20121121T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_paris_to_ay(self):
        """
        ID artemis v1: 21
        """
        self.journey(_from="admin:75056",
                     to="admin:84007", datetime="20121121T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_paris_to_sainte_lizaigne(self):
        """
        ID artemis v1: 22
        """
        self.journey(_from="admin:75056",
                     to="admin:36199", datetime="20121025T120000",
                     walking_speed="0.83", max_duration_to_pt="6000")
