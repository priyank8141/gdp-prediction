import psycopg2
from django.shortcuts import render

conn = psycopg2.connect(database="agriculture", user='postgres', password='priyank8141', host='127.0.0.1',port='5432')
cursor = conn.cursor()
id1 = None
# Create your views here.
def farmerlog(request, id):
    print("this is farmer loggedin page")
    global id1
    id1=id
    print(id1)
    Query = "select * from signup_user where id = %s"
    cursor.execute(Query, (id,))
    records = cursor.fetchall()
    print(records)
    details={
        'id' : records[0][0],
        'name' : records[0][1],
        'email' : records[0][2],
        'mob' : records[0][3],
        'role': records[0][4],
        'von': records[0][5],
        'country': records[0][6],
        'state': records[0][7],
        'city': records[0][8]
    }
    return render(request, "farmer.html",details)
def show_profile(request):
    Query = "select * from signup_user where id = %s"
    cursor.execute(Query, (id1,))
    records = cursor.fetchall()
    print(records)
    details = {
        'id': records[0][0],
        'name': records[0][1],
        'email': records[0][2],
        'mob': records[0][3],
        'role': records[0][4],
        'von': records[0][5],
        'country': records[0][6],
        'state': records[0][7],
        'city': records[0][8]
    }
    return render(request, "profile.html", details)
