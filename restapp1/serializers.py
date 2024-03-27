from rest_framework import serializers
from restapp1.models import Employee

class empSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'