from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from booking.models import Guest, Reservation, Studio, Owner
from booking.serializers import GuestSerializer, CreateOwnerSerializer, StudioSerializer, ReservationSerializer
# Create your views here.
 

class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class CreateStudioViewSet(ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer


class CreateOwnerViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete','head','options']
    queryset = Owner.objects.all()
    serializer_class = CreateOwnerSerializer
    
class ReservationViewSet(ModelViewSet):
        queryset = Reservation.objects.select_related('guest').all()
        serializer_class= ReservationSerializer          