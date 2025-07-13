from plugin.base.template import PluginTemplateView
#from plugin.mixins import PluginConfigMixin

class MyStockAdminView(PluginTemplateView):
    template_name = "my_stock/index.html"
    view_name = "my_stock_panel"
    icon = "fa-boxes"
    title = "My Stock Panel"
