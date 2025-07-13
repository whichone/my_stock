from plugin import InvenTreePlugin
from plugin.mixins import SettingsMixin, PanelMixin
from .settings import MyStockSettings
from .views import MyStockReactView

class MinimalPlugin(PanelMixin, SettingsMixin, InvenTreePlugin):
    NAME = "my_stock"
    TITLE = "My Stock"
    DESCRIPTION = "A simple plugin that adds a custom admin panel"
    VERSION = "0.1"

    SETTINGS = MyStockSettings

    def setup(self):
        # Register the React view
        self.add_view(MyStockReactView)
