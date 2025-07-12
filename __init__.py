from plugin import InvenTreePlugin
from plugin.mixins import AppMixin, SettingsMixin
from .settings import MyStockSettings
from .views import MyStockReactView


class MyStockPlugin(InvenTreePlugin, AppMixin, SettingsMixin):
    NAME = "MyStock"
    TITLE = "Mobile UI"
    SLUG = "my_stock"
    VERSION = "1.0"
    AUTHOR = "Your Name"
    DESCRIPTION = "React-based mobile UI plugin for InvenTree"
    SETTINGS = MyStockSettings

    def setup(self):
        # Optional: Register custom React panels here
        self.add_panel(MyStockReactView)
