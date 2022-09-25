from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from booking.models import Guest
from booking.serializers import CreateGuestSerializer
# Create your views here.
 

class GuestViewSet(ModelViewSet):

    queryset = Guest.objects.all()
    serializer_class = CreateGuestSerializer