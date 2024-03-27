from django.shortcuts import render
from restapp6.serializer import CustomerSerializer
from restapp6.models import Customer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


# Create your views here.
class CustomerList(GenericAPIView, ListModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class CustomerCreate(GenericAPIView, CreateModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CustomerRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class CustomerUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class CustomerDelete(GenericAPIView, DestroyModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class Retrive_Update_Delete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class List_Create(GenericAPIView, ListModelMixin,CreateModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




