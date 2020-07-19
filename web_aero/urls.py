"""web_aero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url,include
from aero import views
from django.views.generic import ListView, DetailView

from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.revamp,name='revamp'),
    url(r'events/$',views.events ,name='events'),
    url(r'gallery/$',views.gallery ,name='gallery'),
    url(r'addblogs/$',views.addblogs, name='addblogs'),
    url(r'blogs/$',views.blogs, name='blogs'),
    path('aeromodelling-club/blogs/<int:pk>/',views.gblog, name='gblog'),
    
]
