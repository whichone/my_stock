from plugin.views import PluginReactView


class MyStockReactView(PluginReactView):
    name = "MyStock UI"
    icon = "fas fa-mobile-alt"
    title = "Mobile UI"
    description = "A React panel for mobile-friendly stock management"
