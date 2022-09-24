from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=255,unique= True)
    email = models.EmailField(unique=True,null=True)
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date= models.DateField(auto_now_add=True, null=True)

    USERNAME_FIELD = 'username'
    