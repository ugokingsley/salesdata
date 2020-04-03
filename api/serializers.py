from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets, permissions
from sales.models import *

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SalesDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SalesData
        fields = ['invoice', 'stockcode', 'description', 'quantity', 'invoicedate', 'price', 'customerid']