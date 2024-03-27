from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from restapp1.models import Employee
from restapp1.serializers import empSerializers

# Create your views here.
class empdetails(APIView):
    def get(self, request):
        emp =Employee.objects.all()
        serializers = empSerializers(emp, many=True)
        return Response(serializers.data)
    def post(self):
        pass

