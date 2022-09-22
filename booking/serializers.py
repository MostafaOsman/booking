from rest_framework import serializers
from rest_framework.serializers import DecimalField
from rest_framework.serializers import ModelSerializer

from booking.models import Customer, Studio

class AddressSerializer(serializers.ModelSerializer):
    


class StudioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Studio
        fields= ['number_of_guests','address','price']
        #number_of_guests= serializers.IntegerField(read_only=True)
        #address= serializers.CharField(read_only=True)
        #price= serializers.DecimalField(read_only=True)

class CustomerSerializer(serializers.ModelSerializer):
    adress = serializers.
    class Meta:
        model = Customer
        fields = ['user_name','email','first_name','last_name','birth_date']



