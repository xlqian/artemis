from artemis.test_mechanism import ArtemisTestFixture, dataset


@dataset(["bibus"])
class TestBibus(ArtemisTestFixture):
    """
    """
    def test_bibus_01(self):
        self.journey(_from="stop_area:BIB:SA:527",
                     to="stop_area:BIB:SA:9", datetime="20041214T070000",
                     datetime_represents="arrival", walking_speed="0.83", max_duration_to_pt="1200")

    def test_bibus_02(self):
        self.journey(_from="stop_area:BIB:SA:336",
                     to="stop_area:BIB:SA:123", datetime="20041215T080000",
                     datetime_represents="arrival", walking_speed="0.83", max_duration_to_pt="1200")

    def test_bibus_03(self):
        self.journey(_from="stop_area:BIB:SA:1202",
                     to="stop_area:BIB:SA:236", datetime="20041215T160000",
                     datetime_represents="arrival", walking_speed="0.83", max_duration_to_pt="1200")

    def test_bibus_04(self):
        """
        test_bibus_03 with different walking speed
        """
        self.journey(_from="stop_area:BIB:SA:1202",
                     to="stop_area:BIB:SA:236", datetime="20041215T160000",
                     datetime_represents="arrival", walking_speed="0.75", max_duration_to_pt="1333")

    def test_bibus_05(self):
        self.journey(_from="stop_area:BIB:SA:139",
                     to="stop_area:BIB:SA:236", datetime="20041214T080000",
                     datetime_represents="arrival", walking_speed="0.75", max_duration_to_pt="1333")

    def test_bibus_06(self):
        self.journey(_from="stop_area:BIB:SA:313",
                     to="stop_area:BIB:SA:470", datetime="20041217T070000",
                     walking_speed="0.83", max_duration_to_pt="1200")

    def test_bibus_07(self):
        self.journey(_from="stop_area:BIB:SA:1204",
                     to="stop_area:BIB:SA:236", datetime="20041214T080000",
                     datetime_represents="arrival", walking_speed="0.83", max_duration_to_pt="1200")

    def test_bibus_08(self):
        self.journey(_from="stop_area:BIB:SA:512",
                     to="stop_area:BIB:SA:363", datetime="20041215T140000",
                     walking_speed="0.83", max_duration_to_pt="1200")

    def test_bibus_09(self):
        self.journey(_from="stop_area:BIB:SA:288",
                     to="stop_area:BIB:SA:180", datetime="20041214T070000",
                     datetime_represents="arrival", walking_speed="0.83", max_duration_to_pt="1200")

    def test_bibus_10(self):
        self.journey(_from="stop_area:BIB:SA:255",
                     to="stop_area:BIB:SA:470", datetime="20041216T070000",
                     walking_speed="0.83", max_duration_to_pt="1200")

    def test_bibus_11(self):
        self.journey(_from="stop_area:BIB:SA:313",
                     to="stop_area:BIB:SA:170", datetime="20050607T114200",
                     datetime_represents="arrival", walking_speed="0.83", max_duration_to_pt="1200")

