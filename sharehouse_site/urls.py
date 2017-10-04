"""sharehouse_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from share_house import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index_reg, name="index_reg"),
    url(r'^login$', views.index, name="index"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^meeting$', views.meeting, name="meeting"),
    url(r'^static$', views.test2, name="test2"),
]