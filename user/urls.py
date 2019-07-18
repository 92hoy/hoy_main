# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.user_info, name='user_info'),

    # url(r'^course_manage/list/$', views.course_manage_list, name='course_manage_list'),
    # url(r'^progress/list/(?P<course_seq>.*?)$', views.progress_list, name='progress_list'),
]
