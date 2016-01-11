# encoding: utf-8

DATA_DIR = "/artemis/data"

CITIES_INPUT_FILE = DATA_DIR + "/france_boundaries.osm.pbf"

DATASET_PATH_LAYOUT = DATA_DIR + "/{dataset}/"

NAV_FILE_PATH_LAYOUT = "/srv/ed/data/{dataset}/data.nav.lz4"

API_POINT_PREFIX = 'navitia/'

REFERENCE_FILE_PATH = '/artemis/references'

RESPONSE_FILE_PATH = '/artemis/output'

JORMUNGANDR_DB = 'dbname=jormungandr user=jormungandr host=artemis_db password=jormungandr'

CITIES_DB = 'dbname=cities user=navitia host=artemis_db password=password'

KIRIN_API = 'http://kirin:9090'