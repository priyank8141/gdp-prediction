
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('organizationlog/<int:id>', views.organizationlog , name="organizationlog"),
    path('orgprofile', views.orgprofile, name="orgprofile"),
    path('orgnotification', views.orgnotification, name="orgnotification"),
    path('orglogout', views.orglogout , name="orglogout"),

]
