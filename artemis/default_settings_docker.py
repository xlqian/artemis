# encoding: utf-8

TYR_DIR = "/srv/tyr"

DATASET_PATH_LAYOUT = "/artemis/data/{dataset}/"

NAV_FILE_PATH_LAYOUT = "/srv/ed/data/{dataset}/data.nav.lz4"

NEW_FUSIO_FILE_PATH_LAYOUT = "/srv/fusio/source/{dataset}/NAVITIART/databases.zip"

RESPONSE_FILE_PATH = 'output'

REFERENCE_FILE_PATH = 'reference'

API_POINT_PREFIX = 'navitia/'

JORMUNGANDR_DB = 'dbname=jormungandr user=jormungandr host=postgis password=jormungandr'

LOGGER = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] [%(levelname)5s] %(message)s',
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
