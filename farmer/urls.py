
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('farmerlog/<int:id>', views.farmerlog, name="farmerlog"),
    path('farmer_profile', views.farmer_profile, name="farmer_profile"),
    path('farmer_request', views.farmer_request, name="farmer_request"),
    path('requestfarmer', views.request_farmer, name="requestfarmer"),
    path('farmerlogout', views.farmerlogout, name="farmerlogout"),
]
