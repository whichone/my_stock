from plugin.settings import PluginSettings, PluginSetting

class MyStockSettings(PluginSettings):
    def setup(self):
        return {
            'enable_feature': PluginSetting(
                description='Enable the mobile UI feature',
                default=True,
                validator=bool
            )
        }
