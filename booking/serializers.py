from ast import Add
from wsgiref import validate
from rest_framework import serializers
from rest_framework.serializers import DecimalField
from rest_framework.serializers import ModelSerializer
from .models import Address, Owner, Studio, Guest, Reservation
from rest_framework import serializers
from django.db import transaction


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=  Address
        fields= ['city','district','building_number']


class GuestSerializer(serializers.ModelSerializer):
    http_method_names = ['get','post','patch','delete']
    address = AddressSerializer()
    class Meta:
        model = Guest 
        fields=['id','username','password','email','first_name','last_name','birth_date','address']
        
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        with transaction.atomic():
            address = Address.objects.create(**address_data)
            guest=Guest.objects.create(address_id= address.id, **validated_data)
            #guest.address = address
        return guest
    
            
    
    def update(self,instance, validated_data):
        address_data = validated_data.pop('address')
        address = instance.address
    #'birth_date'
        instance.username = validated_data.get('username',instance.username)
        instance.password = validated_data.get('password',instance.password)
        instance.email = validated_data.get('email',instance.email)
        instance.username = validated_data.get('username',instance.username)
        instance.first_name= validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.birth_date = validated_data.get('birth_date',instance.birth_date)
        instance.save()
        #'city','district','building_number'
        address.city = address_data.get('city',address.city)
        address.district = address_data.get('district',address.district)
        address.building_number = address_data.get('building_number',address.building_number)
        address.save()

        return instance






class StudioSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Studio
        fields= ['id','number_of_guests','address','price']


    def create(self, validated_data):
        address_data= validated_data.pop('address')
        with transaction.atomic():
            address = Address.objects.create(**address_data)
            studio = Studio.objects.create(address_id = address.id ,**validated_data)
            studio.address=address
            return studio       
        

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address') # new data
        address = instance.address

        instance.number_of_guests = validated_data.get('number_of_guests',instance.number_of_guests)
        instance.price = validated_data.get('price',instance.price)
        instance.save()

        address.city = address_data.get('city',address.city)
        address.district = address_data.get('district',address.district)
        address.building_number = address_data.get('building_number',address.building_number)
        address.save()
        return instance

class CreateOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=  Owner
        fields= ['id','username','password','email','first_name','last_name','birth_date','role']

   

class SimpleGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model= Guest
        exclude = ['password','email','first_name','last_name','birth_date','address']






class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields= ['start_date','end_date']






 








