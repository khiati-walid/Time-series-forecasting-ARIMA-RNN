from rest_framework import serializers
from .models import Sales, Client, Employee


class SalesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sales
        fields = ['id','file']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id','FullName','Wilaya','Email','PhoneNumber','Function']


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','FullName','Wilaya','Email','PhoneNumber','Function']

	