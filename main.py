from plugin import InvenTreePlugin
from plugin.mixins import SettingsMixin, UserInterfaceMixin

class MyPlugin(SettingsMixin, UserInterfaceMixin, InvenTreePlugin):
    NAME = "my_plugin"
    TITLE = "My Plugin"
    DESCRIPTION = "A plugin with settings and a basic UI"
    VERSION = "0.1"

    SETTINGS = {
        'ENABLED': {
            'name': 'Enable Feature',
            'description': 'Enable something useful',
            'validator': bool,
            'default': True,
        }
    }

    def get_user_interface_url(self):
        return "index.html"
