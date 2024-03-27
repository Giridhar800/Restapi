from django.db import models

# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    mail = models.EmailField(max_length=30)
    age = models.IntegerField()

