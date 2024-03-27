from django.shortcuts import render
from restapp8.models import Manager
from restapp8.serializer import ManagerSerializer
from rest_framework import viewsets

# Create your views here.
# class ManagerModelViewSet(viewsets.ModelViewSet):
#     queryset = Manager.objects.all()
#     serializer_class = ManagerSerializer

class ManagerModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
