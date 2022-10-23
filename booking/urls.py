from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework_nested import routers
 
from .views import GuestViewSet
from pprint import pprint



router = routers.DefaultRouter()
router.register('guest',views.GuestViewSet,'guest')
router.register('studio',views.StudioViewSet,'studio')
router.register('owner',views.CreateOwnerViewSet,'owner')
router.register('employee',views.EmployeeViewSet,'employee')
router.register('reservation',views.ReservationViewSet,'reservation')

employee_router = routers.NestedDefaultRouter(router, 'employee', lookup = 'employee')
employee_router.register('studio', views.StudioViewSet, basename = 'employee-studio')




urlpatterns = router.urls