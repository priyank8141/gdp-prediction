import psycopg2
from django.http import HttpResponseRedirect
from django.shortcuts import render
from organization.models import Problem
import pandas as pd

def search_weather(country,state,city):
     weather_data = pd.read_excel(r'E:\agri datanalysis\temp_forecast.xlsx',sheet_name=0,header=0,index_col=False,keep_default_na=True)
     print(weather_data.head())
     co=country
     st=state
     ci=city
     loc=ci+', '+st+', '+co
     print(loc)
     rslt_df = weather_data[weather_data['Loc'] == loc]
     rslt_df=rslt_df[['Loc','Date','Rice','Wheat','Cotton','Jute','Tea']]
     resulthtml = rslt_df.to_html(classes='table1 table', index=False)
     # resulthtml.replace('<tr>', '<tr style="text-align: center;">')
     # print(resulthtml)

     # write html to file
     text_file = open("templates/prediction1.html", "w")
     text_file.write(resulthtml)
     text_file.close()


# Create your views here.
def farmeruser(request):
    userdata = request.session.get('userdata')
    co=userdata['country']
    st= userdata['state']
    di= userdata['district']
    search_weather(co,st,di)
    return render(request, "farmer.html", userdata)

def farmerprofile(request):
    userdata = request.session.get('userdata')
    return render(request, "farmerprofile.html", userdata)

def farmerreport(request):
    userdata = request.session.get('userdata')
    print(userdata['username'])
    if (request.method == 'POST'):
            subject = request.POST['subject']
            detailprob = request.POST['problem']
            ins = Problem(name=userdata['username'],email=userdata['email'],mobile=userdata['mobile'],role=userdata['role'],von=userdata['von'],country=userdata['country'],state=userdata['state'],district=userdata['district'],subject=subject,detailproblem=detailprob,)
            ins.save()
            message= 'Problem Reported successfully'
            userdata['message'] = message
            print(userdata)
            return render(request, "request.html", userdata)
    else:
            return render(request, "request.html", userdata)

def fapredict(request):
    userdata = request.session.get('userdata')
    if (request.method == 'POST'):
        co = request.POST['country']
        st = request.POST['state']
        ci = request.POST['city']
        search_weather(co, st, ci)
    return render(request, "farmer.html",userdata)