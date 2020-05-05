import os
import subprocess
import docker
import requests
import yaml
import jinja2
import pytest
import logging
from retrying import retry
from artemis.configuration_manager import config
from docopt import docopt


COMPOSE_PROJECT_NAME = "navitia"
COMPOSE_BASE_COMMAND = "TAG=dev KIRIN_TAG=master docker-compose -f docker-compose.yml -f kirin/docker-compose_kirin.yml"
LOGS_DIR_PATH = os.path.join(config["RESPONSE_FILE_PATH"], "logs")

logger = logging.getLogger("NG_ORCHESTRATOR")


def check_argument_path(arg: str):
    if arg not in config:
        raise Exception("{} needs to be set".format(arg))
    if not os.path.isdir(config[arg]):
        raise Exception("{} isn't a valid path".format(config[arg]))


def get_compose_containers_list():
    """
    :return: a list of all containers created with docker-compose
    """
    all_containers_list = docker.DockerClient(version="auto").containers.list(all)
    return list(
        x for x in all_containers_list if COMPOSE_PROJECT_NAME in x.attrs["Name"]
    )


@retry(stop_max_delay=3000000, wait_fixed=2000)
def wait_for_cities_db():
    """
    When initializing docker-compose containers, cities db is the last step in instance configuration
    :return: when cities db is upgraded and reachable
    """
    logger.debug("Wait for cities db upgrade...")
    query = config["URL_TYR"] + "/v0/cities/status"
    response = requests.get(query)
    if response.status_code != 200:
        raise Exception("Cities not reachable")
    else:
        logging.debug(" -> Cities Responding")


@retry(stop_max_delay=3000000, wait_fixed=2000)
def wait_for_instance_configuration():
    """
    When creating a new coverage with a Kraken, the 'instance_configurator' container is recreated and executed again to create the new instance in db
    :return: when the instance is configured
    """

    @retry(stop_max_delay=2000000, wait_fixed=2000)
    def wait_for_instance_configuration_status(status):
        docker_list = get_compose_containers_list()
        instance_config_container = next(
            (x for x in docker_list if "instances_configurator" in x.name), None
        )
        if instance_config_container:
            if instance_config_container.status != status:
                raise Exception(
                    "instances_configurator status: {actual} - Expected: {expected}".format(
                        actual=instance_config_container.status, expected=status
                    )
                )
        else:
            logger.warning("No 'instances_configurator' container found")

    wait_for_instance_configuration_status("running")
    wait_for_instance_configuration_status("exited")


# Unused for now!
@retry(stop_max_delay=3000000, wait_fixed=2000)
def wait_for_cities_job_completion():
    logger.debug("Wait for cities job completion...")
    query = config["URL_TYR"] + "/v0/cities/status"
    response = requests.get(query)
    if response.status_code != 200:
        raise Exception("Cities not reachable")
    else:
        last_job = response.text["latest_job"]
        if "state" not in last_job:
            raise Exception("Cities db job not created yet")
        elif last_job["state"] == "running":
            raise Exception("Cities db job in progress")
        else:
            logger.debug("cities job done!")


@retry(stop_max_delay=3000000, wait_fixed=2000)
def wait_for_kraken_stop(kraken_name):
    """
    :param kraken_name: The name of the Kraken running for a specific coverage
    :return: when the Kraken container is stopped
    """
    docker_list = get_compose_containers_list()
    kraken_container = next((x for x in docker_list if kraken_name in x.name), None)
    if kraken_container:
        if kraken_container.status == "running":
            raise Exception("Kraken still running...")
        else:
            logger.debug(
                "Container {} : Status: {}".format(
                    kraken_container.name, kraken_container.status
                )
            )
    else:
        logger.warning("No container found for {}".format(kraken_name))


def wait_for_docker_removal(kraken_name):
    """
    :param kraken_name: The name of the Kraken running for a specific coverage
    :return: when the Kraken container is removed
    """
    logger.debug("Waiting to stop and remove {}".format(kraken_name))

    @retry(stop_max_delay=3000000, wait_fixed=2000)
    def wait_for_kraken_removal():
        docker_list = get_compose_containers_list()
        if next((x for x in docker_list if kraken_name in x.name), None):
            raise Exception("Kraken not yet removed...")

    wait_for_kraken_removal()


def init_dockers(pull, logs):
    """
    Run docker containers with no instance
    Create 'jormungandr' and 'cities' db
    :param pull: update Docker images by pulling them from Dockerhub
    :param logs: store logs in an output folder
    """
    if pull:
        pull_command = "{} pull".format(COMPOSE_BASE_COMMAND)
        child = subprocess.Popen(pull_command, shell=True)
        # Wait for the process to end
        child.communicate()
        status = child.returncode
        if status:
            logger.warning(
                "Error occurred when pulling images frm Dockerhub \n-> Proceeding with available images"
            )

    upCommand = "{} up -d --remove-orphans".format(COMPOSE_BASE_COMMAND)
    subprocess.Popen(upCommand, shell=True)
    wait_for_cities_db()

    if logs:
        # Create logs folder
        if os.path.isdir(LOGS_DIR_PATH):
            os.removedirs(LOGS_DIR_PATH)
        else:
            os.makedirs(LOGS_DIR_PATH)


def launch_coverages(coverages, logs):
    instances_path = os.path.join(config["DOCKER_COMPOSE_PATH"], "artemis/")
    instances_list = os.path.join(instances_path, "artemis_custom_instances_list.yml")
    if not os.path.isfile(instances_list):
        logger.error("Couldn't find instances list at {}".format(instances_list))
        return

    # Load instance Jinja2 template
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(config["DOCKER_COMPOSE_PATH"])
    )
    try:
        template = env.get_template("docker-instances.jinja2")
    except jinja2.TemplateNotFound:
        logger.error("ERROR: Couldn't find template")
        return

    has_failures = False
    # Read the yaml file to get instances
    with open(instances_list, "r") as stream:
        data = yaml.load(stream)

        if coverages:
            list_of_coverages = []
            for coverage_to_run in coverages:
                coverage_to_add = [x for x in data["instances"] if coverage_to_run in x]
                if not coverage_to_add:
                    logger.warning("No coverage matches '{}'".format(coverage_to_run))
                else:
                    list_of_coverages.extend(
                        [x for x in data["instances"] if coverage_to_run in x]
                    )
        else:
            list_of_coverages = data["instances"]

        if not list_of_coverages:
            logger.error("No instance to run!".format(coverage_to_run))
        else:
            for instance in list_of_coverages:
                logger.info("-> Instance read : {}".format(instance))
                # Create file for docker-compose
                instance_name = list(instance)[0]
                instance_file_name = "docker-instance-" + instance_name + ".yml"
                instance_file = os.path.join(instances_path, instance_file_name)
                logger.debug("Create : {}".format(instance_file))

                with open(instance_file, "w") as docker_instance:
                    instance_render = [instance_name]
                    kraken_env_parameters = (
                        instance[instance_name]["kraken_env"]
                        if "kraken_env" in instance[instance_name]
                        else []
                    )
                    jormun_env_parameters = (
                        instance[instance_name]["jormun_env"]
                        if "jormun_env" in instance[instance_name]
                        else ""
                    )
                    docker_instance.write(
                        template.render(
                            instances=instance_render,
                            kraken_env=kraken_env_parameters,
                            jormun_env=jormun_env_parameters,
                        )
                    )

                # Create and start containers
                kraken_name = "kraken-" + instance_name
                upInstanceCommand = "{base} -f {instance_file} up -d --remove-orphans {kraken_name} instances_configurator".format(
                    base=COMPOSE_BASE_COMMAND,
                    instance_file=instance_file,
                    kraken_name=kraken_name,
                )
                logger.debug("Run : {}".format(upInstanceCommand))
                subprocess.Popen(upInstanceCommand, shell=True)

                # Wait for the containers to be ready
                logger.info("Wait for {} docker configuration".format(instance_name))
                wait_for_instance_configuration()

                # Run pytest
                test_class = instance[instance_name]["test_class"]
                logger.info("Run {} test".format(test_class))
                pytest_command = [config["TEST_PATH"], "-m", test_class, "--tb=no"]
                pytest_command.append("--junitxml=output.xml") if logs else None
                p = pytest.main(pytest_command)
                # Check 'pytest.ExitCode.OK' which is 0. Enum available from version > 5
                if p != 0:
                    has_failures = True

                if logs:
                    # Store logs for each coverage
                    instance_logs_dir = os.path.join(LOGS_DIR_PATH, instance_name)
                    os.makedirs(instance_logs_dir)
                    docker_list = get_compose_containers_list()
                    for container in docker_list:
                        file_path = os.path.join(
                            instance_logs_dir, "{}.txt".format(container.name[:-2])
                        )
                        log_file = open(file_path, "w")
                        log_file.write(container.logs().decode())
                    # Store pytest results
                    os.replace(
                        "output.xml",
                        os.path.join(instance_logs_dir, "{}.xml".format(instance_name)),
                    )

                logger.info("Wait for {} docker removal".format(instance_name))
                # Delete instance container
                # The command is divided in 2 separate commands to be handled on old versions of docker/docker-compose
                stopCommand1 = "{base} -f {instance_file} stop {kraken_name}".format(
                    base=COMPOSE_BASE_COMMAND,
                    instance_file=instance_file,
                    kraken_name=kraken_name,
                )
                subprocess.Popen(stopCommand1, shell=True)
                logger.debug("Run : {}".format(stopCommand1))
                wait_for_kraken_stop(kraken_name)

                stopCommand2 = "{base} -f {instance_file} rm -f {kraken_name}".format(
                    base=COMPOSE_BASE_COMMAND,
                    instance_file=instance_file,
                    kraken_name=kraken_name,
                )
                subprocess.Popen(stopCommand2, shell=True)
                logger.debug("Run : {}".format(stopCommand2))
                wait_for_docker_removal(kraken_name)

                # Delete docker-compose instance file
                logger.debug("Remove instance file {}".format(instance_file))
                os.remove(instance_file)

    return has_failures


def docker_clean():
    """
    Stop and remove all containers
    """
    logger.info("Cleaning...")

    @retry(stop_max_delay=3000000, wait_fixed=2000)
    def wait_for_containers_stop():
        if get_compose_containers_list():
            raise Exception("Containers still running...")

    # Stop and remove containers
    downCommand = "{} down -v --remove-orphans".format(COMPOSE_BASE_COMMAND)
    subprocess.Popen(downCommand, shell=True)

    wait_for_containers_stop()


script_doc = """
Artemis Docker Orchestrator

Usage:
    docker_orchestrator.py test [<coverage>...] [-p | --pull] [-l | --logs]
    docker_orchestrator.py clean

Options:
    -h  --help  Help (obviously...)
    -p  --pull  Pull images from Dockerhub
    -l  --logs  Store containers logs in folder
"""
if __name__ == "__main__":
    args = docopt(script_doc, version="0.0.1")

    if args["test"]:
        check_argument_path("DOCKER_COMPOSE_PATH")
        check_argument_path("TEST_PATH")

        os.chdir(config["DOCKER_COMPOSE_PATH"])

        store_logs = args["-l"] | args["--logs"]

        init_dockers(args["-p"] | args["--pull"], store_logs)

        f = launch_coverages(args["<coverage>"], store_logs)

    if args["clean"] or args["test"]:
        docker_clean()

    if f:
        raise Exception("Some tests FAILED")
