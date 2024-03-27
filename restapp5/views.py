from django.shortcuts import render
from rest_framework.views import APIView
from restapp5.serializer import ManagerSerializer
from rest_framework.response import Response
from rest_framework import status
from restapp5.models import Manager

# Create your views here.
class ManagerAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            m = Manager.objects.get(id=id)
            serializer = ManagerSerializer(m)
            return Response(serializer.data)
        m = Manager.objects.all()
        serializer = ManagerSerializer(m, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data inserted'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        m = Manager.objects.get(pk=id)
        serializer = ManagerSerializer(m, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data is updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        m = Manager.objects.get(pk=id)
        serializer = ManagerSerializer(m, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'partially updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        m = Manager.objects.get(pk=id)
        m.delete()
        return Response({'message':'record deleted sucussfully'})



