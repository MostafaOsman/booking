from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from booking.models import Employee, Guest, Reservation, Studio, Owner, Studio
from booking.serializers import GuestSerializer, CreateOwnerSerializer, StudioSerializer, ReservationSerializer, SimpleReservationSerializer, EmployeeSerializer, SimpleEmployeeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
 

class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer




class StudioViewSet(ModelViewSet):
    
    http_method_names = ['get','post','patch','delete','head','options']
    def get_queryset(self):
        return Studio.objects.filter(owner_id= self.request.user.id)    
    def get_permissions(self):
        if self.request.method in ['PATCH','DELETE']:
            return [IsAdminUser()]   
        return [IsAuthenticated()]

            #elif request.method== 'PUT':
            #    serializer = CreateOwnerSerializer(owner,data=request.data) 
            #    serializer.is_valid(raise_exception=True)
            #    serializer.save()
            #    return Response(serializer.data)

    serializer_class = StudioSerializer

class CreateOwnerViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete','head','options']
    queryset = Owner.objects.all()
    serializer_class = CreateOwnerSerializer

  
             

class ReservationViewSet(ModelViewSet):
    #permission_classes = [IsAdminUser]
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ReservationSerializer
        elif self.request.method == 'GET':
            return SimpleReservationSerializer
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Reservation.objects.all()    
        return Reservation.objects.filter(guest_id = self.request.user.id)            
     
    
class EmployeeViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EmployeeSerializer
        elif self.request.method == 'GET':
            return SimpleEmployeeSerializer
    def get_queryset(self):
        return Employee.objects.all()
        
    #def get_queryset(self):    
    #    return Employee.objects.filter(studio_d = self.request.studio.id)
        
    
