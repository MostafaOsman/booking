from email.policy import default
from time import timezone
from typing import Generic
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

class Address(models.Model):
    city= models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    building_number= models.PositiveIntegerField()
   

USER = get_user_model()

class Guest(USER):
    address= models.ForeignKey(Address,on_delete= models.CASCADE)

class Owner(USER):
    pass

class Studio(models.Model):
    title= models.CharField(max_length=255)
    number_of_guests= models.PositiveIntegerField(default=1)
    address = models.OneToOneField(Address,on_delete=models.CASCADE)
    price= models.DecimalField(max_digits=6,
    decimal_places=2, validators= [MinValueValidator(1)])
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE,related_name='studios')

    def __str__(self) -> str:
        return self.title
    


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
    adults = models.PositiveIntegerField(default=0)
    children = models.PositiveIntegerField(default=0)
    check_in= models.DateTimeField()
    check_out= models.DateTimeField()

