"""Restproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest1/', include('restapp1.urls')),
    path('rest2/', include('restapp2.urls')),
    path('rest3/', include('restapp3.urls')),
    path('rest4/', include('restapp4.urls')),
    path('rest5/', include('restapp5.urls')),
    path('rest6/', include('restapp6.urls')),
    path('rest7/', include('restapp7.urls')),
    path('rest8/', include('restapp8.urls')),
    path('', include('restapp9.urls')),
]
