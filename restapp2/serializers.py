from rest_framework import serializers

class EmpSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    ename = serializers.CharField(max_length=20)
    eaddress = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30)