import os
import logging
from plugin import InvenTreePlugin
from plugin.mixins.settings import SettingsMixin

# Get the directory where this file (plugin.py) resides
PLUGIN_DIR = os.path.dirname(os.path.abspath(__file__))

# Log file inside plugin folder
log_path = os.path.join(PLUGIN_DIR, 'my_stock_plugin.log')

logger = logging.getLogger('my_stock')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(log_path)
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)

class MinimalPlugin(SettingsMixin, InvenTreePlugin):
    NAME = "my_stock"
    TITLE = "My Stock"
    DESCRIPTION = "A simple plugin with settings"
    VERSION = "0.1"

    SETTINGS = {
        'API_ENABLE': {
            'name': 'API Functionality',
            'description': 'Enable remote API queries',
            'validator': bool,
            'default': True,
        }
    }

    def setup(self):
        logger.debug(">>> MinimalPlugin setup called")
