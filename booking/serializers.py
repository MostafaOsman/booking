from rest_framework import serializers
from rest_framework.serializers import DecimalField
from rest_framework.serializers import ModelSerializer
from .models import Address, Studio, Guest


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



class CreateGuestSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Guest 
        fields=['username','password','email','first_name','last_name','birth_date','address'] 

    def create(self, validated_data):
        address_data= validated_data.pop('address')
        address = Address.objects.create(**address_data)
        validated_data['address'] =address
        return super().create(validated_data)





