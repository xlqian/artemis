import os
import subprocess
import docker
import requests
import yaml
import jinja2
import pytest

from retrying import retry
from artemis.configuration_manager import config


def get_containers_list():
    return docker.DockerClient(version='auto').containers.list()


@retry(stop_max_delay=3000000, wait_fixed=2000)
def wait_for_jormun():
    query = config['URL_JORMUN']+'/v1/status'
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
    query = config['URL_TYR']+'/v0/cities/status'
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
        if next((x for x in docker_list if kraken_name in x.name), None):
            raise Exception("Kraken still running...")

    wait_for_kraken_stop()


def init_dockers():
    """
    Run docker containers with no instance
    Create 'jormungandr' and 'cities' db
    """
    upCommand = "TAG=dev docker-compose -f docker-compose.yml -f kirin/docker-compose_kirin.yml up -d --remove-orphans"
    subprocess.Popen(upCommand, shell=True)
    wait_for_cities_db()


def launch_coverages():
    if not config['DOCKER_COMPOSE_PATH']:
        raise Exception("DOCKER_COMPOSE_PATH needs to be set")
    instances_path = os.path.join(config['DOCKER_COMPOSE_PATH'], "artemis/")
    instances_list = os.path.join(instances_path, "artemis_custom_instances_list.yml")
    test_path = os.getenv('ARTEMIS_TEST_PATH')

    # Load instance Jinja2 template
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(config['DOCKER_COMPOSE_PATH']))
    try:
        template = env.get_template('docker-instances.jinja2')
    except jinja2.TemplateNotFound:
        print ("ERROR: Couldn't find template")
        return

    # Read the yaml file to get instances
    with open(instances_list, 'r') as stream:
        data = yaml.load(stream)

        for instance in data['instances']:
            # Create file for docker-compose
            instance_name = list(instance)[0]
            instance_file_name = "docker-instance-" + instance_name + ".yml"
            instance_file = os.path.join(instances_path, instance_file_name)
            print("Create : {}".format(instance_file))

            with open(instance_file, 'w') as docker_instance:
                instance_render = [instance_name]
                env_parameters = instance[instance_name]['env'] if 'env' in instance[instance_name] else []
                docker_instance.write(template.render(instances=instance_render, env=env_parameters))

            # Create and start containers
            upInstanceCommand = "TAG=dev docker-compose -f docker-compose.yml -f kirin/docker-compose_kirin.yml -f " + instance_file + " up -d --remove-orphans kraken-" + instance_name + " instances_configurator"
            subprocess.Popen(upInstanceCommand, shell=True)
            # Wait for the containers to be ready
            wait_for_jormun()

            test_class = instance[instance_name]['test_class']
            # Run pytest
            pytest_cmd = test_path + " -k " + test_class

            print("\n ----> RUN TESTS for {} \n     - CMD : {}\n".format(instance_name, pytest_cmd))
            pytest.main([test_path, '-k', test_class])

            # Delete instance container
            kraken_name = "kraken-" + instance_name
            stopCommand = "TAG=dev docker-compose -f docker-compose.yml -f kirin/docker-compose_kirin.yml -f " + instance_file + " rm -sfv kraken-" + instance_name
            subprocess.Popen(stopCommand, shell=True)
            wait_for_docker_stop(kraken_name)

            # Delete docker-compose instance file
            print("Remove instance file {}".format(instance_file))
            os.remove(instance_file)


def docker_clean():
    """
    Stop and remove all containers
    """
    @retry(stop_max_delay=3000000, wait_fixed=2000)
    def wait_for_containers_stop():
        if get_containers_list():
            raise Exception("Containers still running...")

    # Stop and remove containers
    downCommand = "TAG=dev docker-compose -f docker-compose.yml -f kirin/docker-compose_kirin.yml down -v --remove-orphans"
    subprocess.Popen(downCommand, shell=True)

    wait_for_containers_stop()


if __name__ == '__main__':
    os.chdir(config['DOCKER_COMPOSE_PATH'])

    init_dockers()

    launch_coverages()

    docker_clean()
