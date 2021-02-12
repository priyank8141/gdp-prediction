import psycopg2
from django.shortcuts import render
from organization.models import Problem
import pandas as pd

conn = psycopg2.connect(database="agriculture", user='postgres', password='priyank8141', host='127.0.0.1',port='5432')
cursor = conn.cursor()
details = {}

def search_weather(country,state,city):
     weather_data = pd.read_excel(r'E:\agri datanalysis\temp_forecast.xlsx',sheet_name=0,header=0,index_col=False,keep_default_na=True)
     print(weather_data.head())
     co=country
     st=state
     ci=city
     loc=ci+', '+st+', '+co
     # print(loc)
     rslt_df = weather_data[weather_data['Loc'] == loc]
     rslt_df=rslt_df[['Date','Rice','Wheat','Cotton','Jute','Tea']]
     resulthtml = rslt_df.to_html(classes='table1 table', index=False)
     # resulthtml.replace('<tr>', '<tr style="text-align: center;">')
     print(resulthtml)

     # write html to file
     text_file = open("templates/prediction.html", "w")
     text_file.write(resulthtml)
     text_file.close()


# Create your views here.
def farmerlog(request, id):
    print("this is farmer loggedin page")
    global details
    print(id)
    Query = "select * from signup_user where id = %s"
    cursor.execute(Query, (id,))
    records = cursor.fetchall()
    print(records)

    co= records[0][7]
    st= records[0][8]
    ci= records[0][9]

    search_weather(co,st,ci)

    details={
        'id': records[0][0],
        'name': records[0][1],
        'email': records[0][2],
        'mob': records[0][3],
        'role': records[0][5],
        'von': records[0][6],
        'country': records[0][7],
        'state': records[0][8],
        'city': records[0][9]
    }


    return render(request, "farmer.html",details)

def farmer_profile(request):
    print(details)
    print(details['name'])
    return render(request, "farmerprofile.html", details)

def farmer_request(request):
    print("this is request page")
    return render(request, "request.html",details)

def request_farmer(request):
    print(details)
    print(details['name'])
    if (request.method == 'POST'):
            username = details['name']
            print(username)
            email = details['email']
            mobile_no = details['mob']
            role = details['role']
            vo_name = details['von']
            country = details['country']
            state = details['state']
            city = details['city']
            subject = request.POST['subject']
            detailprob = request.POST['problem']
            ins = Problem(name=username,email=email,mobile=mobile_no,role=role,von=vo_name,country=country,state=state,district=city,subject=subject,detailproblem=detailprob,)
            ins.save()
            message= 'Problem Reported successfully'
            details['message'] = message
            print(details)
            return render(request, "request.html", details)
    else:
            return render(request, "request.html", details)


def farmerlogout(request):
    global details
    details = {}
    return render(request, "index.html")

