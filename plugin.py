from inventree.plugins import InvenTreePlugin
from inventree.plugins.base.template import PluginTemplateView
from django.urls import path

class MyUIView(PluginTemplateView):
    template_name = "my_stock/index.html"
    title = "Mobile UI"
    icon = "fas fa-mobile-alt"

class MyUIPlugin(InvenTreePlugin):
    NAME = "MyStock"
    TITLE = "Mobile UI"
    SLUG = "my_stock"

    def get_urls(self):
        return [
            path('ui/', MyUIView.as_view(), name='plugin-ui'),
        ]
