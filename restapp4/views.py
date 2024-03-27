from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restapp4.models import Trainer
from restapp4.serializer import TrainerSerializer

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def trainer_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            tr = Trainer.objects.get(id=id)
            serializer = TrainerSerializer(tr)
            return Response(serializer.data)

        tr = Trainer.objects.all()
        serializer = TrainerSerializer(tr, many=True)
        return Response(serializer.data)

    if request.method =='POST':
        serializer = TrainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data inserted"})
        return Response(serializer.errors)

    if request.method =='PUT':
        id = request.data.get('id')
        tr = Trainer.objects.get(pk=id)
        serializer = TrainerSerializer(tr, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data updated"})
        return Response(serializer.errors)

    if request.method =="DELETE":
        id = request.data.get('id')
        tr = Trainer.objects.get(pk=id)
        tr.delete()
        return Response({'message': 'Record deleted'})

