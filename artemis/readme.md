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

``docker-compose -f docker-compose.yml up``

* Add manually the coverage of your choice in /default (you need fusio content in a .zip folder and the osm.pbf file) 

``docker cp <osm.pbf file> navitiadockercompose_tyr_worker_1:/srv/ed/input/default``

``docker cp <fusio.zip folder> navitiadockercompose_tyr_worker_1:/srv/ed/input/default``

* In default_settings.py : URL_JORMUN (it is the beginning of the request so it asks for your Jormun)
* In the x_test.py file, you have to import base_pytest :

``from artemis.artemis import base_pytest``

* In the x_test.py file, make the test class inherit from : TestFixture
* In the x_test.py file, rename the test class by adding ‘Test’ at the beginning

example : Auvergne(object) --> TestAuvergne(TestFixture)
* In the environment configuration, in additional arguments add :

``--skip_cities``
