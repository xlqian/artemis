from artemis.test_mechanism import ArtemisTestFixture, dataset


@dataset(["saintomer"])
class TestSaintOmer(ArtemisTestFixture):
    """
      test "on demand transport"
    """
    def test_saint_omer_01(self):
        """
        IDQuery 0 and 1
        """
        self.journey(_from="admin:62595",
                     to="poi:adm117", datetime="20121206T133500",
                     walking_speed="1", max_duration_to_pt="1000")

    def test_saint_omer_02(self):
        """
        IDQuery 2
        """
        self.journey(_from="poi:adm117",
                     to="admin:62595", datetime="20121206T153500",
                     walking_speed="1", max_duration_to_pt="1000")

    def test_saint_omer_03(self):
        """
        IDQuery 3
        """
        self.journey(_from="admin:62595",
                     to="2.26668185;50.75150538", datetime="20121206T153500",
                     walking_speed="1", max_duration_to_pt="1000")

    def test_saint_omer_04(self):
        """
        IDQuery 4
        """
        self.journey(_from="2.26668185;50.75150538",
                     to="admin:62595", datetime="20121206T153500",
                     walking_speed="1", max_duration_to_pt="1000")

    def test_saint_omer_05(self):
        """
        IDQuery 5
        """
        self.journey(_from="admin:62595",
                     to="stop_area:ASO:SA:1", datetime="20121206T153500",
                     walking_speed="1", max_duration_to_pt="1000")

    def test_saint_omer_06(self):
        """
        IDQuery 6
        """
        self.journey(_from="stop_area:ASO:SA:1",
                     to="admin:62595", datetime="20121206T153500",
                     walking_speed="1", max_duration_to_pt="1000")

    def test_saint_omer_07(self):
        """
        IDQuery 7
        """
        self.journey(_from="admin:62765",
                     to="admin:62458", datetime="20121120T101500",
                     walking_speed="1", max_duration_to_pt="1000")

    def test_saint_omer_08(self):
        """
        IDQuery 8
        """
        self.journey(_from="admin:62458",
                     to="admin:62765", datetime="20121120T101500",
                     walking_speed="1", max_duration_to_pt="1000")

