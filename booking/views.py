from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from booking.models import Guest, Reservation, Studio, Owner
from booking.serializers import GuestSerializer, CreateOwnerSerializer, StudioSerializer, ReservationSerializer, SimpleReservationSerializer
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
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ReservationSerializer
        elif self.request.method == 'GET':
            return SimpleReservationSerializer    
    queryset = Reservation.objects.all() 
    
        
    
