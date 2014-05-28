from artemis.test_mechanism import ArtemisTestFixture, dataset


@dataset(["airport-01"])
class TestAirport1(ArtemisTestFixture):

    def test_airport_01_01(self):
        self.journey(_from="stop_area:AI1:SA:AIRPORTAIRPORT",
                     to="stop_area:AI1:SA:AIRPORTLYS", datetime="20120904T0700")

    def test_airport_01_02(self):
        self.journey(_from="stop_area:AI1:SA:AIRPORTAMS",
                     to="stop_area:AI1:SA:AIRPORTAIRPORT", datetime="20120904T0900")

    def test_airport_01_03(self):
        self.journey(_from="stop_area:AI1:SA:AIRPORTAIRPORT",
                     to="stop_area:AI1:SA:AIRPORTCLY", datetime="20120908T1000")

    def test_airport_01_04(self):
        self.journey(_from="stop_area:AI1:SA:AIRPORTAIRPORT",
                     to="stop_area:AI1:SA:AIRPORTMRS", datetime="20120908T1200")

