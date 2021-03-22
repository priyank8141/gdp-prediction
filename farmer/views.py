import os
import time
import json
import psycopg2
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import render

from home.decorator import role_required
from organization.models import Problem
import pandas as pd


def search_weather(country,state,city):
     # weather_data = pd.read_excel(r'E:\agri datanalysis\forecast data.xlsx',sheet_name=0,header=0,index_col=False,keep_default_na=True)
     df = pd.read_csv(r'E:\agri datanalysis\forecastdata.csv')
     print(df)

     # wheat pred
     def rice(mxt, mit, r, ):
         if mit >= 15 and mxt <= 32 and r <= 1000:
             return "It's a Great Climate you can"
         else:
             if mit < 15:
                 return "The temperature will not be suitable. It'll go too low!"
             elif mxt > 32:
                 return "The temperature will not be suitable. It'll go too High!"
             else:
                 return "It'll be a Heavy Rainfall"

     # wheat pred
     def wheat(mxt, mit, r, ):
         if mit >= 2 and mxt <= 35 and r <= 80:
             return "It's a Great Climate you can"
         else:
             if mit < 2:
                 return "The temperature will not be suitable. It'll go too low!"
             elif mxt > 35:
                 return "The temperature will not be suitable. It'll go too High!"
             else:
                 return "It'll be a Heavy Rainfall"

     # cotton pred
     def cotton(mxt, mit, r, ):
         if mit >= 10 and mxt <= 35 and r <= 150:
             return "It's a Great Climate you can"
         else:
             if mit < 10:
                 return "The temperature will not be suitable. It'll go too low!"
             elif mxt > 35:
                 return "The temperature will not be suitable. It'll go too High!"
             else:
                 return "It'll be a Heavy Rainfall"

     # jute pred
     def jute(mxt, r, ):
         if r <= 250 and mxt >= 25:
             return "It's a Great Climate you can"
         else:
             if mxt < 25:
                 return "The temperature will not be suitable. It'll go too low!"
             else:
                 return "It'll be a Heavy Rainfall"

     # cotton pred
     def tea(mxt, mit, r, ):
         if mit >= 20 and mxt <= 32 and r <= 300:
             return "It's a Great Climate you can"
         else:
             if mit < 20:
                 return "The temperature will not be suitable. It'll go too low!"
             elif mxt > 32:
                 return "The temperature will not be suitable. It'll go too High!"
             else:
                 return "It'll be a Heavy Rainfall"

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
     print(df)
     df = df[['Loc', 'Date', 'Rice', 'Wheat', 'Cotton', 'Jute', 'Tea']]

     # def color_text(val):
     #     color = ""
     #     if val == "Temp will go very low":
     #         color = 'red'
     #     elif val == "Temp will go very high":
     #         color = 'red'
     #     elif val == "Heavy Rainfal":
     #         color = 'red'
     #     elif val == "Safe":
     #         color = 'green'
     #
     #     return 'color: %s' % color

     # df = df.style.applymap(color_text) \
     #     .set_table_attributes('border="1" class="dataframe table table1"')
     # dfhtml = df.render()
     print(df)
     # return df
     # resulthtml = df.to_html(classes='table1 table', index=False)
     json_records = df.reset_index().to_json(orient='records')
     data = []
     data = json.loads(json_records)
     print(df)
     return data
     # print(df)
     # resulthtml.replace('<tr>', '<tr style="text-align: center;">')
     # print(resulthtml)

     # # write html to file
     # if os.path.exists("templates/prediction.html"):
     #    os.remove("templates/prediction.html")
     #    print("file deleted")
     #    cache.clear()
     #    # time.sleep(5)
     # else:
     #     print("The file does not exist")
     #
     # if os.path.exists("templates/prediction.html"):
     #    print("file still exists")
     # else:
     #     text_file = open("templates/prediction.html", "w")
     #     text_file.write(df)
     #     print("file success written")
     #     text_file.close()
         # time.sleep(15)
         # text_file.truncate(0)


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
        print(di)
        df=search_weather(co,st,di)
        userdata['df'] = df
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
            df = search_weather(co, st, ci)
            userdata['df'] = df

        return render(request, "farmer.html",userdata)