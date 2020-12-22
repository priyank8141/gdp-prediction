import psycopg2
from django.shortcuts import render

# Create your views here.
def organizationlog(request,id):
    print("this is sarpanch loggedin page")
    print(id)
    conn = psycopg2.connect(database="agriculture", user='postgres', password='priyank8141', host='127.0.0.1',port='5432')
    cursor = conn.cursor()
    Query = "select * from signup_user where id = %s"
    cursor.execute(Query, (id,))
    records = cursor.fetchall()
    print(records)
    return render(request, "organization.html")
