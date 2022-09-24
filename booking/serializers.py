from rest_framework import serializers
from rest_framework.serializers import DecimalField
from rest_framework.serializers import ModelSerializer


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['city','district','building_number']


class StudioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Studio
        fields= ['number_of_guests','address','price']
        #number_of_guests= serializers.IntegerField(read_only=True)
        #address= serializers.CharField(read_only=True)
        #price= serializers.DecimalField(read_only=True)

class CustomerSerializer(serializers.ModelSerializer):
    #address = serializers.
    class Meta:
        model = Customer
        fields = ['user_name','email','first_name','last_name','birth_date']




