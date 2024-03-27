from django.db import models

# Create your models here.
class Employee(models.Model):

    ename = models.CharField(max_length=20)
    eaddress = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
