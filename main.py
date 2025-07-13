from plugin import InvenTreePlugin
from plugin.mixins.settings import SettingsMixin

class MinimalPlugin(SettingsMixin, InvenTreePlugin):
    NAME = "MyStock"
    TITLE = "My Stock"
    DESCRIPTION = "A simple plugin with settings"
    VERSION = "0.2"

    SETTINGS = {
        'API_ENABLE': {
            'name': 'API Functionality',
            'description': 'Enable remote API queries',
            'validator': bool,
            'default': True,
        }
    }

