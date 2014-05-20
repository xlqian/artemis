# encoding: utf-8

RESPONSE_FILE_PATH = 'output'

REFERENCE_FILE_PATH = '/home/antoine/run/artemis'

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
    }
}


