
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('organizationlog/<int:id>', views.organizationlog , name="organizationlog"),

]
