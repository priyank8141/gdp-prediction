from django.contrib.auth.models import User
from django.shortcuts import render

from organization.models import Problem
import matplotlib.pyplot as plt, mpld3
import pandas as pd
import seaborn as sns
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly.subplots import make_subplots

sns.set_style('darkgrid')


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
    gdp = pd.read_excel(r'E:\agri datanalysis\India_statewise_GDP_data_new 1-15.xlsx', sheet_name='Sheet2')
    # print(gdp.Country)

    x = gdp['year crore']

    ## show all states:
    #
    # for Country in gdp:
    #     if Country != 'year crore':
    #         plt.plot(x, gdp[Country], marker='.', label=Country)
            # plot_div=plot([Scatter(x=x,y=gdp[Country],mode='lines',name='test',opacity=0.8,marker_color='green')],output_type='div',include_plotlyjs=False)

    # plot_div=plot(fig,output_type='div',include_plotlyjs=False)

    ## show only 5 states:

    # plt.plot(x,gdp.Punjab,color='r',label='Punjab')
    # plt.plot(x,gdp['DELHI, Haryana & CHANDIGARH'],color='g',label='Haryan, Delhi')
    # plt.plot(x,gdp['Gujarat'],color='b',label='Gujarat')
    # plt.plot(x,gdp['Uttar Pradesh'],color='black',label='Uttar Pradesh')
    # plt.plot(x,gdp['Madhya Pradesh'],color='y',label='Madhya Pradesh')

    # plt.xticks(gdp['year crore'][::2])
    # plt.xlabel('Year', fontdict={'fontname': 'Comic sans MS'})
    # plt.ylabel('GDP in CRORE', fontdict={'fontname': 'Comic sans MS'})
    # plt.legend(loc=2)

    # plt.show()
    # resulthtml = mpld3.fig_to_html(fig)

    data=[{
        'x':x,
        'y':gdp[Col],
        'name':Col
        }
        for Col in gdp
            if Col != 'year crore']

    layout=go.Layout(
    xaxis = dict(title='Year'),
    yaxis = dict(title='GDP in M')
    )
    fig =go.Figure(data=data,layout=layout)
    plot_div=pyo.plot(fig,output_type='div',include_plotlyjs=False)

    userdata['gdpgrowth'] = plot_div
    return render(request, "gdpgrowthstatewise.html", userdata)

def rainvsgdp(request):
    st='Gujarat'
    userdata = request.session.get('userdata')
    if request.method == "POST":
        st = request.POST['state']
    rain = pd.read_excel(r'E:\agri datanalysis\rainfall statewise 1901-15.xlsx')
    gdp1 = pd.read_excel(r'E:\agri datanalysis\India_statewise_GDP_data_new 1-15.xlsx', sheet_name=1)
    xr = rain['SUBDIVISION(MM)']
    # print(xr)
    # print(gdp1.columns)
    yr = rain[st]
    # print(yr)
    # Create combo chart
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(x=xr, y=yr, name="rain"),
        secondary_y=False,
    )
    yg = gdp1[st]

    fig.add_trace(
        go.Scatter(x=xr, y=yg, name="GDP"),
        secondary_y=True,
    )

    fig.update_xaxes(title_text="Year")

    fig.update_yaxes(title_text="Rain in MM", secondary_y=False)
    fig.update_yaxes(title_text="GDP", secondary_y=True)

    plot_div = pyo.plot(fig, output_type='div', include_plotlyjs=False)

    userdata['st'] = st
    userdata['rainvsgdp'] = plot_div
    return render(request, "rainvsgdp.html", userdata)

def exportcrop(request):
    cr = 'BASMATI RICE'
    userdata = request.session.get('userdata')
    if request.method == "POST":
        cr = request.POST['state']
    production = pd.read_excel(r'E:\agri datanalysis\export data 2001-2020.xlsx', sheet_name=1)
    value = pd.read_excel(r'E:\agri datanalysis\export data 2001-2020.xlsx', sheet_name=2)
    xp = production['ProductName and Qty']
    yp = production[cr]

    trace0=go.Bar(
        x=xp,
        y=yp,
        name='production'
    )

    yv = value[cr]
    trace1 = go.Bar(
        x=xp,
        y=yv,
        name='export'
    )
    layout = go.Layout(
        xaxis=dict(title='Year',tickmode = 'linear'),
        yaxis=dict(title='Total Export & Production')
    )

    data=[trace0,trace1]
    fig=go.Figure(data=data,layout=layout)
    plot_div = pyo.plot(fig, output_type='div', include_plotlyjs=False)



    userdata['cr'] = cr
    userdata['exportcrop'] = plot_div
    return render(request, "exportcrop.html", userdata)
