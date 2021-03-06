"""hoy_ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from home import views
from home import urls as home_urls
from user import urls as user_urls
from ws_app import urls as ws_app_urls
urlpatterns = [
    # url(r'^$', views.main_base, name='main_base'),
    url(r'^home/', include(home_urls)),
    url(r'^user/', include(user_urls)),
    url(r'^ws_app/', include(ws_app_urls)),
]
