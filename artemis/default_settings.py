# encoding: utf-8

TYR_DIR = "/srv/tyr"

DATASET_PATH_LAYOUT = "/srv/fusio/source/{dataset}/NAVITIART/"

NAV_FILE_PATH_LAYOUT = "/srv/ed/{dataset}/data.nav.lz4"

RESPONSE_FILE_PATH = 'output'

REFERENCE_FILE_PATH = '/srv/artemis'

JORMUNGANDR_DB = 'dbname=jormungandr user=jormungandr host=localhost password=jormungandr'

LOGGER = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{
        'default': {
            'format': '[%(asctime)s] [%(levelname)5s] [%(process)5s] [%(name)10s] %(message)s',
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


