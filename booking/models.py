from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

class Address(models.Model):
    city= models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    building_number= models.PositiveIntegerField()


USER = get_user_model()

class Guest(USER):
    address = models.OneToOneField(Address, on_delete=models.PROTECT,related_name='address')
    

class Owner(USER):
    pass

class Studio(models.Model):
    id = models.IntegerField(primary_key=True)
    number_of_guests= models.PositiveIntegerField()
    address = models.OneToOneField(Address,on_delete=models.CASCADE)
    price= models.DecimalField(max_digits=6,
    decimal_places=2, validators= [MinValueValidator(1)])
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE,related_name='studios',null=True)


class Reservation(models.Model):
    #a reservation can't be active for two guests on the same studio during the same period
    studio = models.ForeignKey(Studio,on_delete=models.CASCADE,related_name='studio')
    STATUS_ACTIVE= 'A'
    STATUS_NON_ACTIVE= 'N'
    STATUS_CHOICES = [
    #user will see this value
        (STATUS_ACTIVE,'Active'),
        (STATUS_NON_ACTIVE,'Non Active')]
    status = models.CharField(choices=STATUS_CHOICES,default=STATUS_NON_ACTIVE,max_length=50)
    guest = models.ForeignKey(Guest,on_delete= models.CASCADE,related_name='guest')
    start_date= models.DateTimeField()
    end_date= models.DateTimeField()

