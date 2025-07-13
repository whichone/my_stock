from plugin import InvenTreePlugin
from plugin.mixins import SettingsMixin
from .settings import MyStockSettings
#from .views import MyStockReactView


class MinimalPlugin(SettingsMixin, InvenTreePlugin):
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
        },
        'API_KEY': {
            'name': 'API Key',
            'description': 'Security key for accessing remote API',
            'default': '',
            'required': True,
        },
        'API_URL': {
            'name': _('API URL'),
            'description': _('Base URL for remote server'),
            'default': 'http://remote.url/api',
        },
        'CONNECTION': {
            'name': _('Printer Interface'),
            'description': _('Select local or network printer'),
            'choices': [('local','Local printer e.g. USB'),('network','Network printer with IP address')],
            'default': 'local',
        },
        'NUMBER': {
            'name': _('A Name'),
            'description': _('Describe me here'),
            'default': 6,
            'validator': [
                int,
                MinValueValidator(2),
                MaxValueValidator(25)
            ]
        },
        'ASSEMBLY': {
            'name': _('Assembled Part'),
            'description': _('Settings can point to internal database models'),
            'model': 'part.part',
            'model_filters': {
                'active': True,
                'assembly': True
            }
        },
        'GROUP': {
            'name': _('User Group'),
            'description': _('Select a group of users'),
            'model': 'auth.group'
        },
        'HIDDEN_SETTING': {
            'name': _('Hidden Setting'),
            'description': _('This setting is hidden from the automatically generated plugin settings page'),
            'hidden': True,
        }
    }

    #def setup(self):
        #print(">>> MinimalPlugin setup called")
        #self.add_view(MyStockReactView)
