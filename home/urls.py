# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^sign/$', views.sign, name='sign'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^api_bit/$', views.api_bit, name='api_bit'),
    # url(r'^course_manage/list/$', views.course_manage_list, name='course_manage_list'),
    # url(r'^progress/list/(?P<course_seq>.*?)$', views.progress_list, name='progress_list'),
]
