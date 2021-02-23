
from django.contrib import admin
from django.urls import path
from home import views as hm
from farmer import views as fa
from sarpanch import views as sa
from organization import views as org

urlpatterns = [
    path('', hm.show_home, {}),
    path('signupuser', hm.signupuser,name='signupuser'),
    path('loginuser', hm.loginuser,name='loginuser'),
    path('logoutuser', hm.logoutuser,name='logoutuser'),
    path('profileuser', hm.profileuser,name='profileuser'),
    path('farmeruser', fa.farmeruser,name='farmeruser'),
    path('farmerprofile', fa.farmerprofile,name='farmerprofile'),
    path('farmerreport', fa.farmerreport,name='farmerreport'),
    path('fapredict', fa.fapredict,name='fapredict'),
    path('sarpanchuser', sa.sarpanchuser,name='sarpanchuser'),
    path('sarpanchprofile', sa.sarpanchprofile,name='sarpanchprofile'),
    path('sarpanchreport', sa.sarpanchreport,name='sarpanchreport'),
    path('sapredict', sa.sapredict,name='sapredict'),
    path('sarpanchprob', sa.sarpanchprob,name='sarpanchprob'),
    path('sardelete_data/<int:id>/', sa.sardelete_data,name='sardelete_data'),
    path('orguser', org.orguser,name='orguser'),
    path('orgprofile', org.orgprofile,name='orgprofile'),
    path('orgprob', org.orgprob,name='orgprob'),
    path('orgdelete_data/<int:id>/', org.orgdelete_data,name='orgdelete_data'),
    path('gdpgrowthstatewise', org.gdpgrowthstatewise,name='gdpgrowthstatewise'),

]
