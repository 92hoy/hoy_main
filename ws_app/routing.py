# chat/routing.py
from django.conf.urls import url
from . import consumer

websocket_urlpatterns = [
    url(r'^ws/ws_app/(?P<room_name>[^/]+)/$', consumer.ChatConsumer),
]