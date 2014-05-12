import logging


class ArtemisTestFixture:
    """
    Mother class for all integration tests
    """

    @classmethod
    def setup(cls):
        logging.info("Initing the tests {}, let's deploy!"
                     .format(cls.__name__))
        cls.run_tyr()

        cls.run_additional_service()

        cls.read_data()

        cls.pop_krakens()  # this might be removed if tyr manage it (in the read_data process)

        cls.pop_jormungandr()


    @classmethod
    def teardown(cls):
        logging.info("Tearing down the tests {}, time to clean up"
                     .format(cls.__name__))

    @classmethod
    def run_tyr(cls):
        """
        run tyr
        tyr is the conductor of navitia.
        """
        pass


    @classmethod
    def run_additional_service(cls):
        """
        run all services that have to be active for all tests
        """
        pass

    @classmethod
    def read_data(cls):
        """
        Read the different data given by Fusio
        launch the different readers (Fusio2Ed, osm2is, ...) and binarize the data
        """
        pass

    @classmethod
    def pop_krakens(cls):
        pass

    @classmethod
    def pop_jormungandr(cls):
        """
        launch the front end
        """
        pass