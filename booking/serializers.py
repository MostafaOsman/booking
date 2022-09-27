from rest_framework import serializers
from rest_framework.serializers import DecimalField
from rest_framework.serializers import ModelSerializer
from .models import Address, Owner, Studio, Guest, Reservation

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id','city','district','building_number']

class CreateOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=  Owner
        fields= ['id','username','password','email','first_name','last_name','birth_date']


class CreateStudioSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Studio
        fields= ['id','number_of_guests','address','price']

    def create(self, validated_data):
        address_data= validated_data.pop('address')
        address = Address.objects.create(**address_data)
        validated_data['address'] = address
        return super().create(validated_data)   



class CreateGuestSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Guest 
        fields=['id','username','password','email','first_name','last_name','birth_date','address']
        
        def create(self, validated_data):
            address_data= validated_data.pop('address')
            address = Address.objects.create(**address_data)
            validated_data['address'] = address
            return super().create(validated_data) 

class SimpleGuestSerializer(serializers.ModelSerializer):
        class Meta:
            model = Guest 
            fields=['first_name','last_name']





class ReservationSerializer(serializers.ModelSerializer):
    guest = SimpleGuestSerializer()
    class Meta:
        model = Reservation
        fields= ['id','guest','start_date','end_date']


    


 








