import os
import time

import psycopg2
from django.http import HttpResponseRedirect
from django.shortcuts import render

from home.decorator import role_required
from organization.models import Problem
import pandas as pd


def search_weather(country,state,city):
     # weather_data = pd.read_excel(r'E:\agri datanalysis\forecast data.xlsx',sheet_name=0,header=0,index_col=False,keep_default_na=True)
     df = pd.read_csv(r'E:\agri datanalysis\forecastdata.csv', sep=',', index_col=False)

     # wheat pred
     def rice(mxt, mit, r, ):
         if mit >= 15 and mxt <= 32 and r <= 1000:
             return "Safe"
         else:
             if mit < 15:
                 return "Temperature will go very low"
             elif mxt > 32:
                 return "Temperature will go very high"
             else:
                 return "heavy rainfall"

     # wheat pred
     def wheat(mxt, mit, r, ):
         if mit >= 2 and mxt <= 35 and r <= 80:
             return "Safe"
         else:
             if mit < 2:
                 return "Temp will go very low"
             elif mxt > 35:
                 return "Temp will go very high"
             else:
                 return "Heavy Rainfall"

     # cotton pred
     def cotton(mxt, mit, r, ):
         if mit >= 10 and mxt <= 35 and r <= 150:
             return "Safe"
         else:
             if mit < 10:
                 return "Temp will go very low"
             elif mxt > 35:
                 return "Temp will go very high"
             else:
                 return "Heavy Rainfall"

     # jute pred
     def jute(mxt, r, ):
         if r <= 250 and mxt >= 25:
             return "Safe"
         else:
             if mxt < 25:
                 return "Temp will go very low"
             else:
                 return "Heavy Rainfall"

     # cotton pred
     def tea(mxt, mit, r, ):
         if mit >= 20 and mxt <= 32 and r <= 300:
             return "Safe"
         else:
             if mit < 20:
                 return "Temp will go very low"
             elif mxt > 32:
                 return "Temp will go very high"
             else:
                 return "Heavy Rainfall"

     df['Rice'] = df.apply(lambda row: rice(row['max_temp_C'],
                                            row['min_temp C'], row['Rain cm']), axis=1)

     df['Wheat'] = df.apply(lambda row: wheat(row['max_temp_C'],
                                              row['min_temp C'], row['Rain cm']), axis=1)

     df['Cotton'] = df.apply(lambda row: cotton(row['max_temp_C'],
                                                row['min_temp C'], row['Rain cm']), axis=1)

     df['Jute'] = df.apply(lambda row: jute(row['max_temp_C'],
                                            row['Rain cm']), axis=1)

     df['Tea'] = df.apply(lambda row: tea(row['max_temp_C'],
                                          row['min_temp C'], row['Rain cm']), axis=1)

     loc = city+', '+state+', '+country

     sd = "2/2/2021"
     ed = "2/9/2021"
     df = df[(df['Loc'] == loc) & (df['Date'] > sd) & (df['Date'] <= ed)]
     df = df[['Loc', 'Date', 'Rice', 'Wheat', 'Cotton', 'Jute', 'Tea']]

     def color_text(val):
         color = ""
         if val == "Temp will go very low":
             color = 'red'
         elif val == "Temp will go very high":
             color = 'red'
         elif val == "Heavy Rainfal":
             color = 'red'
         elif val == "Safe":
             color = 'green'

         return 'color: %s' % color

     df = df.style.applymap(color_text) \
         .set_table_attributes('border="1" class="dataframe table table1"')


     print(df)
     # resulthtml = df.to_html(classes='table1 table', index=False)
     df_html=df.render()
     # print(df)
     # resulthtml.replace('<tr>', '<tr style="text-align: center;">')
     # print(resulthtml)

     # # write html to file
     # os.remove("templates/prediction.html")
     text_file = open("templates/prediction.html", "w")
     text_file.truncate(0)
     time.sleep(2)
     text_file.write(df_html)
     time.sleep(2)
     text_file.close()


# Create your views here.
@role_required(allowed_roles =["farmer"])
def farmeruser(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
        userdata = request.session.get('userdata')
        co=userdata['country']
        st= userdata['state']
        di= userdata['district']
        search_weather(co,st,di)
        time.sleep(5)
        return render(request, "farmer.html", userdata)



@role_required(allowed_roles =["farmer"])
def farmerprofile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
        userdata = request.session.get('userdata')
        return render(request, "farmerprofile.html", userdata)


@role_required(allowed_roles =["farmer"])
def farmerreport(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
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


@role_required(allowed_roles = ["farmer"])
def fapredict(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
        if (request.method == 'POST'):
            userdata = request.session.get('userdata')
            print("fapred")
            co = request.POST['country']
            st = request.POST['state']
            ci = request.POST['city']
            print(ci)
            search_weather(co, st, ci)
            time.sleep(5)
        return render(request, "farmer.html",userdata)