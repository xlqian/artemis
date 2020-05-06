# Docker Orchestrator

This script allows to run locally Artemis tests on one or several coverages by orchestrating the necessary docker containers.

### How to use

The orchestrator uses [docopt](http://docopt.org/) for its interface:

```
Artemis Docker Orchestrator

Usage:
    docker_orchestrator.py test [<coverage>...] [-p | --pull] [-l | --logs]
    docker_orchestrator.py clean

Options:
    -h  --help  Help (obviously...)
    -p  --pull  Pull images from Dockerhub
    -l  --logs  Store containers logs in folder
```

#### Configuration

Some of the parameters needed by the orchestrator are the same as the ones passed to ArtemisNG, and they aren't supposed to change. So, a [compose_settings file](https://github.com/CanalTP/artemis/blob/master/artemis/compose_settings.py) has been created.
To these parameters must be added:
- TEST_PATH: path to the local [tests](https://github.com/CanalTP/artemis/tree/master/artemis/tests) folder of Artemis
- DOCKER_COMPOSE_PATH: path to the local [docker-compose](https://github.com/CanalTP/navitia-docker-compose) folder
- REFERENCE_FILE_PATH: path to the local [artemis_references](https://github.com/CanalTP/artemis_references) folder
- DATA_DIR: path to the local "artemis-data" folder

#### Commands

With all the parameters in a configuration file, the orchestrator can be run with the command:
    `CONFIG_FILE=<my_config_file> docker_orchestrator.py test`
This command will run all Artemis tests on all coverages.

To run the tests on one or several specific coverages only, run:
    `CONFIG_FILE=<my_config_file> docker_orchestrator.py test <coverage_1> <coverage_2>`

The orchestrator will find the coverages to run in the [instances list](https://github.com/CanalTP/navitia-docker-compose/blob/master/artemis/artemis_custom_instances_list.yml) from the navitia-docker-compose project.
The name of the coverages to be passed in the command above is the key from the instances list.
_ex: airport-01, fr-auv, etc..._

To pull the latest docker images from [Dockerhub](https://hub.docker.com/u/navitia/) before running the tests, the parameter `-p | --pull` can be added to the test command.

The orchestrator also allows to store logs from the tests session. To do so, use the `-l | --logs` parameter with the test command. The logs will be stored in a `logs` folder created in the `RESPONSE_FILE_PATH` folder (by default: <artemis_root>/output).
Here, a folder is created for each coverage run with the XML file from the pytest results and the logs from every containers run.

---

If for some reasons, at the end of the tests session, the docker containers popped are still running, the following command can be used:
    `CONFIG_FILE=<my_config_file> docker_orchestrator clean`



