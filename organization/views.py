
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from home.decorator import role_required
from organization.models import Problem
import matplotlib.pyplot as plt, mpld3
import pandas as pd
import seaborn as sns
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly.subplots import make_subplots

sns.set_style('darkgrid')

@role_required(allowed_roles =["organization"])
def orguser(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
        userdata = request.session.get('userdata')
        return render(request, "organization.html", userdata)

@role_required(allowed_roles =["organization"])
def orgprofile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
        userdata = request.session.get('userdata')
        return render(request, "organizationprofile.html", userdata)


@role_required(allowed_roles =["organization"])
def orgprob(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
        userdata = request.session.get('userdata')
        data = Problem.objects.filter(role='sarpanch')
        userdata['problem'] = data
        return render(request, "orgnoti.html", userdata)


@role_required(allowed_roles =["organization"])
def orgdelete_data(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
        userdata = request.session.get('userdata')
        data = Problem.objects.filter(role='sarpanch')
        userdata['problem'] = data
        if request.method=="POST":
            pi =Problem.objects.get(pk=id)
            pi.delete()
            return render(request, "orgnoti.html", userdata)


@role_required(allowed_roles =["organization"])
def gdpgrowthstatewise(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
        userdata = request.session.get('userdata')
        # cols=[0,1,2,3,4]
        gdp = pd.read_excel(r'E:\agri datanalysis\India_statewise_GDP_data_new 1-15.xlsx', sheet_name='Sheet2')
        # print(gdp.Country)

        # x = gdp['year crore']
        # data=[{
        #     'x':x,
        #     'y':gdp[Col],
        #     'name':Col
        #     }
        #     for Col in gdp
        #         if Col != 'year crore']
        #
        layout=go.Layout(
            xaxis = dict(title='<b>Year</b>'),
            yaxis = dict(title='<b>GDP in M</b>')
        )
        # fig =go.Figure(data=data,layout=layout)
        # plot_div=pyo.plot(fig,output_type='div',include_plotlyjs=False)

        fig =go.Figure(layout=layout)

        for column in gdp.columns.to_list():
            if column != 'year crore':
                fig.add_trace(
                    go.Scatter(
                        x=gdp['year crore'],
                        y=gdp[column],
                        name=column
                    )
                )
        fig.update_layout(
            updatemenus=[go.layout.Updatemenu(
                active=0,
                buttons=list(
                    [dict(label='All',
                          method='update',
                          args=[{'visible': [True, True, True, True,True, True, True, True,True, True, True, True,True, True, True, True,True, True, True, True,True, True, True, True, True]},
                                {'title': 'All',
                                 'showlegend': True}]),
                     dict(label='Andaman and Nicobar Islands',
                          method='update',
                          args=[{'visible': [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
                                # the index of True aligns with the indices of plot traces
                                {'title': 'Andaman and Nicobar Islands',
                                 'showlegend': True}]),
                     dict(label='Arunachal Pradesh',
                          method='update',
                          args=[{'visible': [False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
                                {'title': 'Arunachal Pradesh',
                                 'showlegend': True}]),
                     dict(label='ASSAM & MEGHALAYA',
                          method='update',
                          args=[{'visible': [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
                                {'title': 'ASSAM & MEGHALAYA',
                                 'showlegend': True}]),
                     dict(label='Andhra Pradesh',
                          method='update',
                          args=[{'visible': [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
                                {'title': 'Andhra Pradesh',
                                 'showlegend': True}]),
                     dict(label='Bihar',
                          method='update',
                          args=[{'visible': [False, False, False, False, True, False, False, False, False, False,
                                             False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False]},
                                {'title': 'Bihar',
                                 'showlegend': True}]),
                     dict(label='Chhattisgarh',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, True, False, False, False, False,
                                             False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False]},
                                {'title': 'Chhattisgarh',
                                 'showlegend': True}]),
                     dict(label='DELHI, Haryana & CHANDIGARH',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, True, False, False, False,
                                             False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False]},
                                {'title': 'DELHI, Haryana & CHANDIGARH',
                                 'showlegend': True}]),
                     dict(label='Goa',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, True, False, False,
                                             False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False]},
                                {'title': 'Goa',
                                 'showlegend': True}]),
                     dict(label='Gujarat',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, True, False,
                                             False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False]},
                                {'title': 'Gujarat',
                                 'showlegend': True}]),
                     dict(label='Himachal Pradesh',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, False, True,
                                             False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False]},
                                {'title': 'Himachal Pradesh',
                                 'showlegend': True}]),
                     dict(label='Jammu and Kashmir',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, False, False,
                                             True, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False]},
                                {'title': 'Jammu and Kashmir',
                                 'showlegend': True}]),
                     dict(label='Jharkhand',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, False, False,
                                             False, True, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False]},
                                {'title': 'Jharkhand',
                                 'showlegend': True}]),
                     dict(label='Karnataka',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, False, False,
                                             False, False, True, False, False, False, False, False, False, False,
                                             False, False, False, False, False]},
                                {'title': 'Karnataka',
                                 'showlegend': True}]),
                     dict(label='Kerala',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, True, False, False, False, False, False, False,
                                             False, False, False, False, False]},
                                {'title': 'Kerala',
                                 'showlegend': True}]),
                     dict(label='Madhya Pradesh',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, True, False, False, False, False, False,
                                             False, False, False, False, False]},
                                {'title': 'Madhya Pradesh',
                                 'showlegend': True}]),
                     dict(label='Maharashtra',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False, True, False, False, False, False,
                                             False, False, False, False, False]},
                                {'title': 'Maharashtra',
                                 'showlegend': True}]),
                     dict(label='MANI NAGA MIZO TRIPURA',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False, False, True, False, False, False,
                                             False, False, False, False, False]},
                                {'title': 'MANI NAGA MIZO TRIPURA',
                                 'showlegend': True}]),
                     dict(label='Odisha',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False, False, False, True, False, False,
                                             False, False, False, False, False]},
                                {'title': 'Odisha',
                                 'showlegend': True}]),
                     dict(label='Punjab',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False, False, False, False, True, False,
                                             False, False, False, False, False]},
                                {'title': 'Punjab',
                                 'showlegend': True}]),
                     dict(label='Rajasthan',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False, False, False, False, False, True,
                                             False, False, False, False, False]},
                                {'title': 'Rajasthan',
                                 'showlegend': True}]),
                     dict(label='Sikkim & west bengal',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False, False, False, False, False, False,
                                             True, False, False, False, False]},
                                {'title': 'Sikkim & west bengal',
                                 'showlegend': True}]),
                     dict(label='Tamil Nadu',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False, False, False, False, False, False,
                                             False, True, False, False, False]},
                                {'title': 'Tamil Nadu',
                                 'showlegend': True}]),
                     dict(label='Telangana',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False, False, False, False, False, False,
                                             False, False, True, False, False]},
                                {'title': 'Telangana',
                                 'showlegend': True}]),
                     dict(label='Uttar Pradesh',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, True, False]},
                                {'title': 'Uttar Pradesh',
                                 'showlegend': True}]),
                     dict(label='Uttarakhand',
                          method='update',
                          args=[{'visible': [False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, False, False, False, False, False, False,
                                             False, False, False, False, True]},
                                {'title': 'Uttarakhand',
                                 'showlegend': True}]),
                     ])
            )
            ]),

        plot_div=pyo.plot(fig,output_type='div',include_plotlyjs=False)
        userdata['gdpgrowth'] = plot_div
        return render(request, "gdpgrowthstatewise.html", userdata)


@role_required(allowed_roles =["organization"])
def rainvsgdp(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
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

        fig.update_xaxes(title_text="<b>Year</b>")

        fig.update_yaxes(title_text="<b>Rain in MM</b>", secondary_y=False)
        fig.update_yaxes(title_text="<b>GDP</b>", secondary_y=True)

        plot_div = pyo.plot(fig, output_type='div', include_plotlyjs=False)

        userdata['st'] = st
        userdata['rainvsgdp'] = plot_div
        return render(request, "rainvsgdp.html", userdata)


@role_required(allowed_roles =["organization"])
def exportcrop(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
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
            xaxis=dict(title='<b>Year</b>',tickmode = 'linear'),
            yaxis=dict(title='<b>Total Export & Production</b>')
        )

        data=[trace0,trace1]
        fig=go.Figure(data=data,layout=layout)
        fig.update_layout(barmode='group', xaxis_tickangle=-45)
        plot_div = pyo.plot(fig, output_type='div', include_plotlyjs=False)

        userdata['cr'] = cr
        userdata['exportcrop'] = plot_div
        return render(request, "exportcrop.html", userdata)


@role_required(allowed_roles =["organization"])
def prod(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
        userdata = request.session.get('userdata')
        production = pd.read_excel(r'E:\agri datanalysis\crop production.xlsx')
        xp = production['year wheat cotton in 1000MT cotton 1000 lb bales']

        data=[go.Scatter(x= xp,
            y= production[Col],
            name= Col,
            mode='lines+markers',
            opacity=0.8
                         )
            for Col in production
                if Col != 'year wheat cotton in 1000MT cotton 1000 lb bales']


        layout = go.Layout(
            xaxis=dict(title='<b>Year</b>',
            tickmode = 'linear',
            tick0 = 1960,
            dtick = 5),
            yaxis=dict(title='<b>Production</b>')
        )

        fig = go.Figure(data=data, layout=layout)
        # plot_div=pyo.plot([go.Scatter(x=xp,y=production[Col],mode='lines+markers',name='Col',opacity=0.8,)for Col in production
        #         if Col != 'year wheat cotton in 1000MT cotton 1000 lb bales'],output_type='div',include_plotlyjs=False)
        plot_div = pyo.plot(fig, output_type='div', include_plotlyjs=False)

        userdata['prod'] = plot_div
        return render(request, "production.html", userdata)


@role_required(allowed_roles =["organization"])
def fertilizeruse(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
        userdata = request.session.get('userdata')
        ferti = pd.read_excel(r'E:\agri datanalysis\use of fertilizer.xlsx',)
        # print(ferti)
        xf = ferti['Year 1000 Tonnes']
        data = [go.Scatter(
            x= xf,
            y= ferti[Col],
            name= Col,
            mode='lines+markers',
            opacity=0.8
        )

            for Col in ferti
                if Col != 'Year 1000 Tonnes']

        layout = go.Layout(
            xaxis=dict(title='<b>Year</b>',
            tickmode = 'linear',
            tick0 = 2000,
            dtick = 2),
            yaxis=dict(title='<b>Fertilizers</b>')
        )
        fig = go.Figure(data=data, layout=layout)
        plot_div = pyo.plot(fig, output_type='div', include_plotlyjs=False)

        userdata['fertilizeruse'] = plot_div
        return render(request, "fertilizersuse.html", userdata)