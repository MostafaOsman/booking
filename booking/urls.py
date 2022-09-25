from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework_nested import routers
 
from .views import GuestViewSet
from pprint import pprint



router = routers.DefaultRouter()
router.register('guests',views.GuestViewSet,'guests')

urlpatterns = router.urls 