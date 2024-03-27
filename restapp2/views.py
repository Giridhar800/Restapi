from django.shortcuts import render, HttpResponse
from restapp2.models import Employee
from restapp2.serializers import EmpSerializer
from rest_framework.renderers import JSONRenderer


# Create your views here.
def emp_details(request, pk):
    emp = Employee.objects.get(id=pk)
    serializers = EmpSerializer(emp)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data, content_type='application/json')
def emp_all_details(request):
    emp = Employee.objects.all()
    serializers = EmpSerializer(emp, many=True)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data, content_type='application/json')

