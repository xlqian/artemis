from artemis.test_mechanism import ArtemisTestFixture, dataset


@dataset(["kraken"])
class TestDummyJourney(ArtemisTestFixture):

    def test_call_to_end_point(self):
        self.api("")

    def test_call_to_journey_url(self):
        self.journey_url("from=0.6633598999999322%3B47.401366"
                     "&to=0.7548520000000281%3B47.414169&datetime=20140512T183000"
                     "&datetime_represents=departure&count=3")

    def test_call_to_journey(self):
        self.journey(_from="0.6633598999999322;47.401366",
                     to="0.7548520000000281;47.414169", datetime="20140512T183000", count=3)

        #twice the same call should not be a problem
        self.journey(_from="0.6633598999999322;47.401366",
                     to="0.7548520000000281;47.414169", datetime="20140512T183000", count=3)
