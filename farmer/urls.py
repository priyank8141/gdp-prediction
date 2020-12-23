
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('farmerlog/<int:id>', views.farmerlog , name="farmerlog"),
    path('profile', views.farmer_profile , name="farmer_profile"),
    path('request', views.farmer_request , name="farmer_request"),
    path('requestsend', views.request_process , name="requestprocess"),
    path('logout', views.farmerlogout , name="farmerlogout"),
]
