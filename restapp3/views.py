from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from restapp3.serializers import ManagerSerializer
from django.views import View
from restapp3.models import Manager
from django.utils.decorators import method_decorator
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class empdata(View):
    def get(self, request, *args, **kwargs):
            if request.method == 'GET':
                jsondata = request.body
                stream = io.BytesIO(jsondata)
                py_data = JSONParser().parse(stream)
                id = py_data.get('id', None)
                if id is not None:
                    emp = Manager.objects.get(id=id)
                    serializer = ManagerSerializer(emp)
                    jsondata = JSONRenderer().render(serializer.data)
                    return HttpResponse(jsondata, content_type='application/json')
                emp = Manager.objects.all()
                serializer = ManagerSerializer(emp, many=True)
                jsondata = JSONRenderer().render(serializer.data)
                return HttpResponse(jsondata, content_type='application/json')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            jsondata = request.body
            stream = io.BytesIO(jsondata)
            py_data = JSONParser().parse(stream)
            serializer = ManagerSerializer(data=py_data)
            if serializer.is_valid():
                serializer.save()
                result = {'message': 'data inserted into database'}
                jsondata = JSONRenderer().render(result)
                return HttpResponse(jsondata, content_type='application/json')
            jsondata = JSONRenderer().render(serializer.errors)
            return HttpResponse(jsondata, content_type='application/json')


    def put(self, request, *args, **kwargs):
        if request.method == 'PUT':
            jsondata = request.body
            stream = io.BytesIO(jsondata)
            py_data = JSONParser().parse(stream)
            id = py_data.get('id')
            emp = Manager.objects.get(id=id)
            serializer = ManagerSerializer(emp, data=py_data)
            if serializer.is_valid():
                serializer.save()
                result = {'message': 'data inserted into database'}
                jsondata = JSONRenderer().render(result)
                return HttpResponse(jsondata, content_type='application/json')
            jsondata = JSONRenderer().render(serializer.errors)
            return HttpResponse(jsondata, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        if request.method == 'DELETE':
            jsondata = request.body
            stream = io.BytesIO(jsondata)
            py_data = JSONParser().parse(stream)
            id = py_data.get('id')
            emp = Manager.objects.get(id=id)
            emp.delete()
            result = {'message': 'Data deleted from database'}
            jsondata = JSONRenderer().render(result)
            return HttpResponse(jsondata, content_type='application/json')



