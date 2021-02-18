
from django.contrib import admin
from django.urls import path
from home import views as hm
from farmer import views as fa
from sarpanch import views as sa

urlpatterns = [
    path('', hm.show_home, {}),
    path('signupuser', hm.signupuser,name='signupuser'),
    path('loginuser', hm.loginuser,name='loginuser'),
    path('logoutuser', hm.logoutuser,name='logoutuser'),
    path('profileuser', hm.profileuser,name='profileuser'),
    path('farmeruser', fa.farmeruser,name='farmeruser'),
    path('farmerprofile', fa.farmerprofile,name='farmerprofile'),
    path('farmerrequest', fa.farmerrequest,name='farmerrequest'),
    path('fapredict', fa.fapredict,name='fapredict'),
    path('sarpanchuser', sa.sarpanchuser,name='sarpanchuser'),
    path('sarpanchprofile', sa.sarpanchprofile,name='sarpanchprofile'),
    path('sarpanchrequest', sa.sarpanchrequest,name='sarpanchrequest'),
    path('sapredict', sa.sapredict,name='sapredict'),
    path('sarpanchnoti', sa.sarpanchnoti,name='sarpanchnoti'),

]
