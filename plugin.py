from plugin import InvenTreePlugin
from django.urls import path

class MyUIView(PluginTemplateView):
    template_name = "my_stock/index.html"
    title = "Mobile UI"
    icon = "fas fa-mobile-alt"

class MyStock(InvenTreePlugin):
    NAME = "MyStock"
    TITLE = "Mobile UI"
    SLUG = "my_stock"

    def get_urls(self):
        return [
            path('ui/', MyUIView.as_view(), name='plugin-ui'),
        ]
