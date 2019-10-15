import logging
import inspect
import psycopg2
import requests
import os

import artemis.utils as utils

from artemis.configuration_manager import config

logger = logging.getLogger(__name__)


# given a cursor on a db, and table names separated by a comma (ex: "tata, toto, titi")
def truncate_tables(cursor, table_names_string):
    logger.debug("query db: TRUNCATE {} CASCADE ;".format(table_names_string))
    cursor.execute("TRUNCATE {} CASCADE ;".format(table_names_string))


# the time cost is around 1.3s on artemis platform
def clean_kirin_db():
    logger.info("cleaning kirin database")
    conn = psycopg2.connect(config['KIRIN_DB'])
    try:
        cur = conn.cursor()
        cur.execute("SELECT relname FROM pg_stat_user_tables WHERE relname != 'alembic_version';")
        tables = cur.fetchall()

        truncate_tables(cur, ', '.join(e[0] for e in tables if e[0] not in ("layer", "topology")))

        conn.commit()

        cur.execute(
            "INSERT INTO contributor SELECT 'realtime.sherbrooke','ca-qc-sherbrooke','token_to_be_modified',"
            "'feed_url_to_be_modified','gtfs-rt'"
        )
        cur.execute(
            "INSERT INTO contributor SELECT 'realtime.cots','sncf','token_to_be_modified',"
            "'feed_url_to_be_modified','cots'"
        )
        conn.commit()
        logger.debug("kirin db purge done")
    except:
        logger.exception("problem with kirin db")
        conn.close()
        assert False, "problem while cleaning kirin db"
    conn.close()


class CommonTestFixture(object):


    def get_dataset_name(self):
        mro = inspect.getmro(self.__class__)
        return "Test{}".format(mro[1].__name__)

    def get_scenario_name(self):
        mro = inspect.getmro(self.__class__)
        return mro[0].data_sets[0].scenario

    def get_reference_suffix_path(self):
        return os.path.join(self.get_dataset_name(), self.get_scenario_name())

    def get_reference_filename_prefix(self):
        """
        When there is multiple calls to request_compare within one test function
          the name of the reference file for the first call is `func_name`
          For the (n+1)th call, the name of the reference file is `func_name_n`
        """
        func_name = utils.get_calling_test_function()

        if self.nb_call_to_request_compare <= 1:
            return func_name
        else :
            assert self.nb_call_to_request_compare > 1
            return "{}_{}".format(func_name, self.nb_call_to_request_compare - 1)

    def get_test_name(self):
        path = os.path.join(self.get_reference_suffix_path(),
                            self.get_reference_filename_prefix())
        return str(path)

 
    def get_reference_file_path(self):
        filename = "{}.json".format(self.get_reference_filename_prefix())
        return os.path.join(config['REFERENCE_FILE_PATH']
                            , self.get_reference_suffix_path()
                            , filename )

    @staticmethod
    def _send_cots(cots_file_name):
        r = requests.post(config['KIRIN_API'] + '/cots',
                          data=utils.get_rt_data(cots_file_name).encode('UTF-8'),
                          headers={'Content-Type': 'application/json;charset=utf-8'})
        r.raise_for_status()

    def send_and_wait(self, rt_file_name):
        """
        Send a COTS and wait until the data is reloaded
        :param rt_file_name: name of the real-time feed file (obviously)
        """
        if self.check_ref:
            return

        if len(self.data_sets) > 1:
            logger.warning(" >1 data_set for test class !!!")
        coverage = self.data_sets[0].name
        last_rt_data_loaded = self.get_last_rt_loaded_time(coverage)
        self._send_cots(rt_file_name)
        self.wait_for_rt_reload(last_rt_data_loaded, coverage)
