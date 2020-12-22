
from django.contrib import admin
from django.urls import path, include

import farmer
from . import views

urlpatterns = [

    path('login', views.show_login, name="login"),
    path('logprocess', views.logproess,name='logproess'),

]
