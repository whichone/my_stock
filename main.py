from plugin import InvenTreePlugin
from plugin.mixins import SettingsMixin
from plugin.base.template import PluginTemplateView
from plugin.mixins import PluginConfigMixin

class MyPluginFrontendView(PluginConfigMixin, PluginTemplateView):
    template_name = "my_plugin/index.html"
    view_name = "my_plugin_panel"
    icon = "fa-plug"
    title = "My Plugin Panel"

class MyPlugin(SettingsMixin, InvenTreePlugin):
    NAME = "my_plugin"
    TITLE = "My Plugin"
    DESCRIPTION = "Simple plugin with settings and a basic UI"
    VERSION = "0.4"

    SETTINGS = {
        'ENABLED': {
            'name': 'Enable Feature',
            'description': 'Enable something useful',
            'validator': bool,
            'default': True,
        }
    }

    def setup(self):
        return [MyPluginFrontendView]
