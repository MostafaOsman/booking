
from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Address(models.Model):
    
    city= models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    building_number= models.PositiveIntegerField()
    #studio_number = models.PositiveIntegerField()

USER = get_user_model()
class Customer(USER):
    address = models.OneToOneField(Address, on_delete=models.deletion.CASCADE)
    
class Studio(models.Model):
    number_of_guests= models.PositiveIntegerField(max_length = 50)
    address = models.OneToOneField(Address,on_delete=models.CASCADE)
    price= models.models.DecimalField(max_digits=6,
    decimal_places=2, validators= [MinValueValidator(1)])

    
