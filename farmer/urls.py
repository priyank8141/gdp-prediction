
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('farmerlog/<int:id>', views.farmerlog , name="farmerlog"),
    path('profile', views.show_profile , name="show_profile"),

]
