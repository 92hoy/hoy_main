from django.conf.urls import url

from . import views

websocket_urlpatterns = [
    url(r'^socket_test/$', views.socket_test),
]