from rest_framework import serializers
from restapp3.models import Manager

# validators
# def starts_with_s(value):
#     if value[0].lower() != 's':
#         raise serializers.ValidationError('Name should starts with letter s')

class ManagerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=30)
    mail = serializers.EmailField(max_length=30)
    age = serializers.IntegerField()

    def create(self, validated_data):
        return Manager.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.mail = validated_data.get('mail', instance.mail)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance

def validate_age(self, value):
    if value > 100:
        raise serializers.ValidationError('Age should not exceed 100')
        return value



