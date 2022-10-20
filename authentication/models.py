from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.models import UserManager

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=255,unique= True)
    email = models.EmailField(unique=True,null=True)
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date= models.DateField(null=True)
    is_staff = models.BooleanField(default=False)
    ROLE_HOST= 'H'
    ROLE_GUEST= 'G'
    ROLE_ADMIN= 'A'
    ROLE_CHOICES = [
    #user will see this value
    (ROLE_HOST,'Host'),
    (ROLE_GUEST,'Guest'),
    (ROLE_ADMIN,'Admin')]

    role = models.CharField(choices=ROLE_CHOICES,default=ROLE_GUEST,max_length=255)
    
    USERNAME_FIELD = 'username'

    objects = UserManager()
    

    
    
    