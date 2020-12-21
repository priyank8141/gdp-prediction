import psycopg2
from django.shortcuts import render, redirect
from .models import user

# Create your views here.

def show_signup(request):
    print("this is signup page")
    return render(request, "signup.html")

def successregister(request):
    print("this is successregister page")
    return render(request, "successregister.html")


conn = psycopg2.connect(database="agriculture", user='postgres', password='priyank8141', host='127.0.0.1', port='5432')
cursor = conn.cursor()

def process(request):
    if (request.method == 'POST'):
        try:
            username = request.POST['username']
            print(username)
            email = request.POST['email']
            mobile_no = request.POST['mobileno']
            gender = request.POST['gender']
            role = request.POST['role']
            vo_name = request.POST['voname']
            country = request.POST['country']
            state = request.POST['state']
            city = request.POST['city']
            password = request.POST['password']
            insertq = '''INSERT INTO SIGNUP_USER(name, email, mobile, gender, role, von, country, state, district, password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            record_to_insert = (username, email, mobile_no, gender, role, vo_name, country, state, city, password)
            cursor.execute(insertq, record_to_insert)
            conn.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully")

        except (Exception, psycopg2.Error) as error:
           print("Failed to insert record error:-", error)

        finally:
            # closing database connection.
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
        context = {
            'message': 'Record inserted successfully'
        }
        return render(request, "login.html", context)
    else:
        return render(request, "signup.html")

