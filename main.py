from plugin import InvenTreePlugin
from plugin.mixins import SettingsMixin
from .views import MyStockAdminView

class MinimalPlugin(SettingsMixin, InvenTreePlugin):
    NAME = "MyStock"
    TITLE = "My Stock"
    DESCRIPTION = "A simple plugin with settings"
    VERSION = "0.3"

    SETTINGS = {
        'API_ENABLE': {
            'name': 'API Functionality',
            'description': 'Enable remote API queries',
            'validator': bool,
            'default': True,
        }
    }

    def setup(self):
        return [
            MyStockAdminView,  # Adds your custom view to the plugin admin panel
        ]

