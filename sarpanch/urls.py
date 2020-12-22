
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('sarpanchlog/<int:id>', views.sarpanchlog , name="sarpanchlog"),

]
