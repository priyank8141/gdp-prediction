
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.show_signup,name='signup'),
    path('process', views.process,name='process'),
    path('successregister', views.successregister,name='successregister'),
]
