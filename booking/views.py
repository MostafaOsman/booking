from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from booking.models import Guest, Reservation, Studio, Owner
from booking.serializers import CreateGuestSerializer, CreateOwnerSerializer, CreateStudioSerializer, ReservationSerializer
# Create your views here.
 

class GuestViewSet(ModelViewSet):

    queryset = Guest.objects.select_related('address').all()
    serializer_class = CreateGuestSerializer



class CreateStudioViewSet(ModelViewSet):
    queryset = Studio.objects.select_related('address').all()
    serializer_class = CreateStudioSerializer


class CreateOwnerViewSet(ModelViewSet):
     queryset = Owner.objects.all()
     serializer_class= CreateOwnerSerializer

class ReservationViewSet(ModelViewSet):
        queryset = Reservation.objects.select_related('guest').all()
        serializer_class= ReservationSerializer          