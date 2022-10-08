from django.contrib import admin
from booking.models import Studio
# Register your models here.

@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
        list_display= ['number_of_guests','address','price']

        
