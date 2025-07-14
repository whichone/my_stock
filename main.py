from plugin import InvenTreePlugin
from plugin.mixins import UserInterfaceMixin
from django.urls import path
from django.http import HttpResponse
from django.views import View

class MyPlugin(UserInterfaceMixin, InvenTreePlugin):
    NAME = "my_plugin"
    TITLE = "My Plugin"
    DESCRIPTION = "A minimal plugin with a built-in interface page"
    VERSION = "0.1"

    def get_custom_urls(self):
        return [
            path('interface/', self.InterfaceView.as_view(), name='my_plugin_interface'),
        ]

    class InterfaceView(View):
        def get(self, request, *args, **kwargs):
            return HttpResponse("""
                <html>
                    <head><title>My Plugin</title></head>
                    <body style="font-family: sans-serif;">
                        <h1>My Plugin Interface</h1>
                        <p>This is a minimal plugin page.</p>
                    </body>
                </html>
            """)
