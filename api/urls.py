from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from api import views
from rest_framework import routers
from .views import UserViewSet, GetAuthToken

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
   
    path('organizer/', views.organizer_list),
    path('organizer_list/', views.organizer_list),
    path('organizer/<int:pk>/', views.organizer_detail),
]