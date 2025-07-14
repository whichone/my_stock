from plugin import InvenTreePlugin
from plugin.mixins import UserInterfaceMixin
from django.urls import path
from django.http import HttpResponse
from django.views import View

class MyPlugin(UserInterfaceMixin, InvenTreePlugin):
    NAME = "my_plugin"
    TITLE = "My Plugin"
    DESCRIPTION = "Minimal plugin with visible tab"
    VERSION = "0.1"

    def get_custom_panels(self, request):
        return [
            {
                'title': 'My Tab',
                'icon': 'fas fa-puzzle-piece',
                'url': 'my_plugin_interface',
            }
        ]

    def get_custom_urls(self):
        return [
            path('interface/', self.InterfaceView.as_view(), name='my_plugin_interface'),
        ]

    class InterfaceView(View):
        def get(self, request, *args, **kwargs):
            return HttpResponse("""
                <div style="padding: 1em; font-family: sans-serif;">
                    <h2>This is my tab</h2>
                    <p>Hello from inside the Plugin Configurations panel!</p>
                </div>
            """)
