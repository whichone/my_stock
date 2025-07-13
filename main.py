from plugin import InvenTreePlugin
from plugin.mixins import SettingsMixin, PluginConfigMixin
from .settings import MyStockSettings
from .views import MyStockReactView

class MyStock(SettingsMixin, PluginConfigMixin, InvenTreePlugin):
    NAME = "my_stock"
    TITLE = "My Stock"
    DESCRIPTION = "A simple plugin that adds a custom admin panel"
    VERSION = "0.1"

    SETTINGS = MyStockSettings

    def setup(self):
        # Register the React view
        print(">>> MinimalPlugin setup called")
        self.add_view(MyStockReactView)
