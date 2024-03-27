from django.contrib import admin
from django.urls import path, include
from restapp9 import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ManagerViewSet', views.ManagerModelViewSet, basename='manager')

urlpatterns = [
    path('', include(router.urls)),
]