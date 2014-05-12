import os
import json
import logging.config
import sys


if 'LOGGER' in os.environ:
    logging.config.dictConfig(os.environ['LOGGER'])
else:  # Default is std out
    handler = logging.StreamHandler(stream=sys.stdout)
    log = logging.getLogger(__name__)
    log.setLevel('INFO')
    log.addHandler(handler)