from plugin import InvenTreePlugin

class MyUIView(PluginTemplateView):
    template_name = "my_stock/index.html"
    title = "Mobile UI"
    icon = "fas fa-mobile-alt"

class MyStock(InvenTreePlugin):
    NAME = "MyStock"
    TITLE = "Mobile UI"
    SLUG = "my_stock"
