from plugin import InvenTreePlugin
from plugin.mixins import SettingsMixin
from django.utils.translation import gettext_lazy as _
#from .settings import MyStockSettings
#from .views import MyStockReactView


class MyStock(SettingsMixin, InvenTreePlugin):
#class MinimalPlugin(SettingsMixin, PluginConfigMixin, InvenTreePlugin):
    NAME = "my_stock"
    TITLE = "My Stock"
    DESCRIPTION = "A simple plugin with settings and a React UI"
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
        print(">>> MinimalPlugin setup called")
        #self.add_view(MyStockReactView)
