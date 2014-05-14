*******
Artemis
*******

Business tests for navitia

Usage
=====

To run the test, run
``python -m py.test artemis/``
in the artemis dir

you can provide a custom config file (if the default_settings.py is not good enough for you) by providing a ``CONFIG_FILE`` environment variable

``CONFIG_FILE=my_conf.py python -m py.test artemis/``