from django.shortcuts import render
from restapp9.models import Manager
from restapp9.serializer import ManagerSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# Create your views here.
class ManagerModelViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]
