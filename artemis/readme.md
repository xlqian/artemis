Artemis Next Generation
=====

Currently working with tests calling the function journey() only once. Only on one coverage (to choose in accordance with the tests).
If a test fails, a folder 'outputs' is created in artemis/artemis/ and reference and response are saved as a file, json format.
Also, if a test fails, differences between both files line per line are shown in the console.


How to use
=====

* launch jormun/tyr/artemis instances' docker containers:
    - to build jormun/tyr's containers, use [docker-compose.yml](https://github.com/CanalTP/navitia-docker-compose/docker-compose.yml)
    - bo build artemis instances' containers, use [docker-artemis-instance.yml](https://github.com/CanalTP/navitia-docker-compose/blob/master/artemis/docker-artemis-instance.yml)(you can also rebuild this file with a jinja template, which is explained in readme)
    - Once you set up all correctly, launch this command: `docker-compose -f docker-compose.yml up -f docker-artemis-instance.yml`

* In default_settings.py : set URL_JORMUN (it is the beginning of the request so it asks for your Jormun)

* In default_settings.py : set URL_TYR (it is the beginning of the request so it asks for your Jormun)

* In default_settings.py : set REFERENCE_FILE_PATH(the path to artemis)

* (Optional )In default_settings.py : set RESPONSE_FILE_PATH

* In the x_test.py file, replace imports by :

``from artemis.test_mechanism import dataset, DataSet, set_scenario``

``from artemis.base_pytest import ArtemisTestFixture``

* In the environment configuration, in additional arguments add :

``--skip_cities``

* If you want to show prints, you can also add this argument :

``-s``

