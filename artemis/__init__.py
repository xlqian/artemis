import logging
import os
import shutil
from configuration_manager import config

logging.getLogger().warn("setup before all")
# clean up the response dir (note, I did not manage to use the setup_module for that)
logging.getLogger().info("removing output dir {}".format(config['RESPONSE_FILE_PATH']))
if os.path.exists(config['RESPONSE_FILE_PATH']):
    shutil.rmtree(config['RESPONSE_FILE_PATH'])