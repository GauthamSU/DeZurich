from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/edit-menu/<slug:slug_title>/', consumers.EditMenuConsumer.as_asgi()),
]