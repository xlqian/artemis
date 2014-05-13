from artemis.test_mechanism import ArtemisTestFixture, dataset


@dataset(["kraken"])
class TestDummy2(ArtemisTestFixture):
    # to test that the init are done correctly and that we can call separatly one test fixture

    def test_call_to_end_point(self):
        self.api("")
