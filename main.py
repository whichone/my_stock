from plugin import InvenTreePlugin
from plugin.mixins import UserInterfaceMixin
from django.urls import path
from django.http import HttpResponse
from django.views import View
from django.utils.translation import gettext_lazy as _

class MyPlugin(UserInterfaceMixin, InvenTreePlugin):
    NAME = "my_plugin"
    TITLE = "My Plugin"
    DESCRIPTION = "A minimal plugin with an interface tab"
    VERSION = "0.1"

    def get_custom_panels(self, request):
        return [
            {
                'title': _('My Tab'),
                'icon': 'fas fa-puzzle-piece',
                'url': 'my_plugin_interface',  # This must match the named URL below
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
                    <h2>My Plugin Interface</h2>
                    <p>This is a custom tab rendered inside the plugin page.</p>
                </div>
            """)
