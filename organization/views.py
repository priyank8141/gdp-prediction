import psycopg2
from django.shortcuts import render

from organization.models import Problem

conn = psycopg2.connect(database="agriculture", user='postgres', password='priyank8141', host='127.0.0.1',port='5432')
cursor = conn.cursor()
details = {}

def organizationlog(request,id):
    print("this is organization loggedin page")
    global details
    print(id)
    Query = "select * from signup_user where id = %s"
    cursor.execute(Query, (id,))
    records = cursor.fetchall()
    print(records)
    details = {
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
    return render(request, "organization.html", details)


def orgprofile(request):
    print(details)
    print(details['name'])
    return render(request, "organizationprofile.html", details)


def orgnotification(request):
    return render(request, "orgnoti.html", details)

def orglogout(request):
    global details
    details = {}
    return render(request, "index.html")
