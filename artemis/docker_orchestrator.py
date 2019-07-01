import os
import subprocess
import docker
import requests
import yaml
import jinja2
import pytest

from retrying import retry

# Path to the docker-compose files
DOCKER_COMPOSE_PATH = os.getenv('ARTEMIS_DOCKER_COMPOSE_PATH')
INSTANCES_PATH = DOCKER_COMPOSE_PATH+"artemis/"
INSTANCES_LIST = INSTANCES_PATH+"artemis_custom_instances_list.yml"
TEST_PATH = os.getenv('ARTEMIS_TEST_PATH', os.getcwd()+'/tests')


def get_containers_list():
    return docker.DockerClient(version='auto').containers.list()


@retry(stop_max_delay=3000000, wait_fixed=2000)
def wait_for_jormun():
    query = 'http://localhost:9191/v1/status'
    response = requests.get(query)
    if response.status_code == 200:
        print(" -> JORMUN Responding")
        print(response.status_code, response.text)
    else:
        raise Exception("JORMUN NOT Responding")


@retry(stop_max_delay=3000000, wait_fixed=2000)
def wait_for_cities_db():
    print("Wait for cities db upgrade...")
    query = 'http://localhost:9898/v0/cities/status'
    response = requests.get(query)
    if response.status_code != 200:
        raise Exception("Cities not reachable")
    else:
        print(" -> Cities Responding")
        print(response.status_code, response.text)


# Unused for now!
@retry(stop_max_delay=3000000, wait_fixed=2000)
def wait_for_cities_job_completion():

    print("Wait for cities job completion...")
    query = 'http://localhost:9898/v0/cities/status'
    response = requests.get(query)
    if response.status_code != 200:
        raise Exception("Cities not reachable")
    else:
        last_job = response.text['latest_job']
        if 'state' not in last_job:
            raise Exception('Cities db job not created yet')
        elif last_job['state'] == 'running':
            raise Exception('Cities db job in progress')
        else:
            print('cities job done!')


def wait_for_docker_stop(kraken_name):
    print("WAITING TO STOP {}".format(kraken_name))

    @retry(stop_max_delay=3000000, wait_fixed=2000)
    def wait_for_kraken_stop():
        docker_list = get_containers_list()
        containers = [x for x in docker_list if kraken_name in x.name]
        if len(containers) > 0:
            raise Exception("Kraken still running...")

    wait_for_kraken_stop()


def docker_clean():
    """
    Stop and remove all containers
    """
    @retry(stop_max_delay=3000000, wait_fixed=2000)
    def wait_for_containers_stop():
        if len(get_containers_list()) > 0:
            raise Exception("Containers still running...")

    # Stop and remove containers
    downCommand = "TAG=dev docker-compose -f docker-compose.yml -f kirin/docker-compose_kirin.yml down -v --remove-orphans"
    subprocess.Popen(downCommand, shell=True)

    wait_for_containers_stop()


def init_dockers():
    """
    Run docker containers with no instance
    Create 'jormungandr' and 'cities' db
    """
    upCommand = "TAG=dev docker-compose -f docker-compose.yml -f kirin/docker-compose_kirin.yml up -d --remove-orphans"
    subprocess.Popen(upCommand, shell=True)
    wait_for_cities_db()

"""
MAIN
"""

if not DOCKER_COMPOSE_PATH:
    print("DOCKER_COMPOSE_PATH needs to be set")
    raise Exception

os.chdir(DOCKER_COMPOSE_PATH)

init_dockers()

# Load instance Jinja2 template
env = jinja2.Environment(loader=jinja2.FileSystemLoader(DOCKER_COMPOSE_PATH))
template = env.get_template('docker-instances.jinja2')

# Read the yaml file to get instances
with open(INSTANCES_LIST, 'r') as stream:
    data = yaml.load(stream)

    for instance in data['instances']:
        # Create file for docker-compose
        instance_name = list(instance)[0]
        instance_file = INSTANCES_PATH+"docker-instance-"+instance_name+".yml"
        print("Create : {}".format(instance_file))

        with open(instance_file, 'w') as docker_instance:
            instance_render = [instance_name]
            env_parameters = instance[instance_name]['env'] if 'env' in instance[instance_name] else []
            docker_instance.write(template.render(instances=instance_render, env=env_parameters))

        # Create and start containers
        upInstanceCommand = "TAG=dev docker-compose -f docker-compose.yml -f kirin/docker-compose_kirin.yml -f "+instance_file+" up -d --remove-orphans kraken-"+instance_name+" instances_configurator"
        subprocess.Popen(upInstanceCommand, shell=True)
        # Wait for the containers to be ready
        wait_for_jormun()

        test_class = instance[instance_name]['test_class']
        # Run pytest
        pytest_cmd = TEST_PATH+" -k " + test_class

        print("\n ----> RUN TESTS for {} \n     - CMD : {}\n".format(instance_name, pytest_cmd))
        pytest.main([TEST_PATH, '-k', test_class])

        # Delete instance container
        kraken_name = "kraken-"+instance_name
        stopCommand = "TAG=dev docker-compose -f docker-compose.yml -f kirin/docker-compose_kirin.yml -f "+instance_file+" rm -sfv kraken-"+instance_name
        subprocess.Popen(stopCommand, shell=True)
        wait_for_docker_stop(kraken_name)

        # Delete docker-compose instance file
        print("Remove instance file {}".format(instance_file))
        os.remove(instance_file)

docker_clean()
