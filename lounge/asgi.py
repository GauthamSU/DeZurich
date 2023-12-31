"""
ASGI config for lounge project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from create_track_orders import routing as order_routing
from menu import routing as menu_routing

websocket_urlpatterns = order_routing.websocket_urlpatterns
# websocket_urlpatterns += menu_routing.websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lounge.settings')

django_asgi_application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        'http': django_asgi_application,
        'websocket': AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        )
    }
)
