# encoding: utf-8

TYR_DIR = "/srv/tyr"

DATA_DIR = "/srv/artemis_data"

CITIES_INPUT_FILE = DATA_DIR + "/france_boundaries.osm.pbf"

DATASET_PATH_LAYOUT = DATA_DIR + "/{dataset}/"

NAV_FILE_PATH_LAYOUT = "/srv/ed/{dataset}/data.nav.lz4"

NEW_FUSIO_FILE_PATH_LAYOUT = "/srv/fusio/source/{dataset}/NAVITIART/databases.zip"

RESPONSE_FILE_PATH = 'output'

REFERENCE_FILE_PATH = 'reference'

API_POINT_PREFIX = ''

KIRIN_API = 'http://localhost:9090'

JORMUNGANDR_DB = 'dbname=jormungandr user=jormungandr host=localhost password=jormungandr'

KIRIN_DB = 'dbname=kirin user=kirin host=localhost password=kirin'

CITIES_DB = 'dbname=cities user=navitia host=localhost password=password'

# Path to my artemis references
PATH_REF = '/home/louis_gaillet/Projets/Artemis/artemis_references/'

# Beginning of the URL : we want the request to go to my own Jormun on my own machine
URL_JORMUN = 'http://127.0.0.1:9191/v1/coverage/default/journeys?'

LOGGER = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{
        'default': {
            'format': '[%(asctime)s] [%(levelname)5s] [%(name)25s] %(message)s',
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        'requests': {
            'handlers': ['default'],
            'level': 'WARN',
            'propagate': True
        },
    }
}
