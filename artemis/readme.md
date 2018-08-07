Goal
=====

    Separating dependencies from Artemis so we can launch a pytest on our personnal computer with our own kraken/jormungandr/tyr.


Results
=====

    Currently working with tests calling the function journey() only once. Only on one coverage (to choose in accordance with the tests).
    If a test fails, a folder 'outputs' is created in artemis/artemis/ and reference and response are saved as a file, json format.
    Also, if a test fails, differences between both files line per line are shown in the console.


How to use
=====

* launch kraken/jormun/tyr from a terminal (from /navitia-docker-compose) :

``docker-compose -f docker-compose.yml up -f additional_navitia_instances.yml``

* In default_settings.py : URL_JORMUN (it is the beginning of the request so it asks for your Jormun)

* In default_settings.py : ARTEMIS_PATH (the path to artemis)

* In the x_test.py file, replace imports by :

``from artemis.test_mechanism import dataset, DataSet, set_scenario``

``from artemis.base_pytest import ArtemisTestFixture``

* In the environment configuration, in additional arguments add :

``--skip_cities``

* If you want to show prints, you can also add this argument :

``-s``

