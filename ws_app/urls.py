# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^socket_test/$', views.socket_test, name='socket_test'),
]
