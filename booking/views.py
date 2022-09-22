from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from booking.serializers import StudioSerializer
from models import Studio


class StudioViewSet(ModelViewSet):
    queryset= Studio.objects.all()
    serializer_class = StudioSerializer