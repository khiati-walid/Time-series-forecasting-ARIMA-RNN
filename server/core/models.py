from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Sales(models.Model):
    file =models.FileField()


class Client(models.Model):
    FullName = models.CharField(max_length=100)
    Wilaya = models.CharField(max_length=50)
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length=50)
    Function = models.CharField(max_length=50)


class Employee(models.Model):
    FullName = models.CharField(max_length=100)
    Wilaya = models.CharField(max_length=50)
    Email = models.EmailField()
    PhoneNumber =models.CharField(max_length=50)
    Function = models.CharField(max_length=50)


