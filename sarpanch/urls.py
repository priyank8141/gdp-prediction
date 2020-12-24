
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('sarpanchlog/<int:id>', views.sarpanchlog , name="sarpanchlog"),
    path('profile', views.show_profile, name="show_profile"),
    path('request', views.show_request, name="show_request"),
    path('requestsend', views.request_process, name="requestprocess"),
    path('notification', views.show_notification, name="notification"),
    path('logout', views.logout , name="logout"),

]
