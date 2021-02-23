from django.contrib.auth.models import User
from django.shortcuts import render

from organization.models import Problem
import matplotlib.pyplot as plt, mpld3
import pandas as pd

import numpy as np
# import ipywidgets as widgets

# %matplotlib inline

def orguser(request):
    userdata = request.session.get('userdata')
    return render(request, "organization.html", userdata)

def orgprofile(request):
    userdata = request.session.get('userdata')
    return render(request, "organizationprofile.html", userdata)


def orgprob(request):
    userdata = request.session.get('userdata')
    data = Problem.objects.filter(role='sarpanch')
    userdata['problem'] = data
    return render(request, "orgnoti.html", userdata)

def orgdelete_data(request,id):
    userdata = request.session.get('userdata')
    data = Problem.objects.filter(role='sarpanch')
    userdata['problem'] = data
    if request.method=="POST":
        pi =Problem.objects.get(pk=id)
        pi.delete()
        return render(request, "orgnoti.html", userdata)

def gdpgrowthstatewise(request):
    userdata = request.session.get('userdata')
    gdp = pd.read_excel(r'E:\agri datanalysis\India_statewise_GDP_data_new 1-15.xlsx', sheet_name='Sheet4')
    # print(gdp.Country)

    fig = plt.figure(figsize=(13, 9))
    x = gdp['year crore']

    ## show all states:

    for Country in gdp:
        if Country != 'year crore':
            plt.plot(x, gdp[Country], marker='.', label=Country)

    ## show only 5 states:

    # plt.plot(x,gdp.Punjab,color='r',label='Punjab')
    # plt.plot(x,gdp['DELHI, Haryana & CHANDIGARH'],color='g',label='Haryan, Delhi')
    # plt.plot(x,gdp['Gujarat'],color='b',label='Gujarat')
    # plt.plot(x,gdp['Uttar Pradesh'],color='black',label='Uttar Pradesh')
    # plt.plot(x,gdp['Madhya Pradesh'],color='y',label='Madhya Pradesh')

    plt.xticks(gdp['year crore'][::2])
    plt.xlabel('Year', fontdict={'fontname': 'Comic sans MS'})
    plt.ylabel('GDP in CRORE', fontdict={'fontname': 'Comic sans MS'})
    plt.legend()

    # plt.show()
    resulthtml = mpld3.fig_to_html(fig)
    userdata['gdpgrowth'] = resulthtml
    return render(request, "gdpgrowthstatewise.html", userdata)