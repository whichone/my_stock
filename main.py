from plugin import InvenTreePlugin
from plugin.mixins import SettingsMixin, PanelMixin
from .settings import MyStockSettings
from .views import MyStockReactView

class MinimalPlugin(PanelMixin, SettingsMixin, InvenTreePlugin):
    NAME = "my_stock"
    TITLE = "My Stock"
    DESCRIPTION = "A simple plugin that adds a custom admin panel"
    VERSION = "0.1"

    def get_custom_panels(self, request):
        return [
            {
                'title': 'Hello World Panel',
                'icon': 'circle',  # Use any Tabler icon name
                'content': '<p>This is a custom panel from the <strong>My Stock</strong>!</p>',
                'enabled': True
            }
        ]


