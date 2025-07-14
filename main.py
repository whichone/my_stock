from inventree.plugin import InvenTreePlugin
from plugin.mixins import SettingsMixin, UserInterfaceMixin


class MyStock(SettingsMixin, UserInterfaceMixin, InvenTreePlugin):
    NAME = "my_stock"
    TITLE = "My Stock"
    DESCRIPTION = "A plugin with settings and a basic UI"
    VERSION = "0.7"

    SETTINGS = {
        'ENABLED': {
            'name': 'Enable Feature',
            'description': 'Enable something useful',
            'validator': bool,
            'default': True,
        }
    }

    def get_user_interface_url(self):
        # Return the entry file inside 'web' folder
        return "index.html"
