from ast import Add
from venv import create
from wsgiref import validate
from rest_framework import serializers
from rest_framework.serializers import DecimalField
from rest_framework.serializers import ModelSerializer
from .models import Address, Employee, Owner, Studio, Guest, Reservation
from rest_framework import serializers
from django.db import transaction
from django.utils import timezone



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
            guest=Guest.objects.create(address_id= address.id, 
            **validated_data)
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
        fields= ['id','title','price','number_of_guests','owner','address']


    def create(self, validated_data):
        # do i create a new address with every studio? yeah so make this step
        #otherwise dont write the pop step like in case of owner
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
        fields= ['id','username','password','email','first_name','last_name','birth_date']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=  Employee
        fields= ['id','username','password','email','first_name','last_name','birth_date','studio']

    

class SimpleOwnerSerializer(serializers.ModelSerializer):
       class Meta:
        model=  Owner
        fields = ['username']

class SimpleStudioSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Studio
        fields= ['title','address']

class SimpleGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields= ['username','email','full_name']
        
    full_name = serializers.SerializerMethodField(method_name='get_full_name')

    def get_full_name(self, guest:Guest):
        return f'{guest.first_name} {guest.last_name}'


class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields= ['adults','children','check_in','check_out','studio','guest']

     
        # studio address bt3o ka data w gwah el owner
        # #guest esm
        # full_name = serializers.SerializerMethodField(method_name='get_full_name')
        


    def validate(self, data):
        check_in = data['check_in']
        check_out = data['check_out']
        studio = data['studio']
        adults = data['adults']
        children = data['children']

        if  (adults+children) > studio.number_of_guests:
            raise serializers.ValidationError("Room can't be booked for this number of guests")
    
        if timezone.now() > check_in:
            raise serializers.ValidationError("check_in date must be today or later")
        

        if timezone.now() > check_out:
            raise serializers.ValidationError("check_in date must be today or later")

        if check_out < check_in:
            raise serializers.ValidationError("check_out date must be later than check_in date")

        return data

     
class SimpleReservationSerializer(serializers.ModelSerializer):
    guest = SimpleGuestSerializer()
    studio = SimpleStudioSerializer()
    class Meta:
        model = Reservation
        fields= ['adults','children','check_in','check_out','studio','guest']


class SimpleEmployeeSerializer(serializers.ModelSerializer):
    studio= SimpleStudioSerializer(many=True)
    class Meta:
        model=  Employee
        fields= ['id','username','password','email','first_name','last_name','birth_date','studio']

       



 








