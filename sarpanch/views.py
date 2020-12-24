import psycopg2
from django.shortcuts import render

from organization.models import Problem

conn = psycopg2.connect(database="agriculture", user='postgres', password='priyank8141', host='127.0.0.1',port='5432')
cursor = conn.cursor()
details = {}
# Create your views here.
def sarpanchlog(request,id):
    print("this is sarpanch loggedin page")
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
    return render(request, "sarpanch.html", details)


def show_profile(request):
    print(details)
    print(details['name'])
    return render(request, "sarpanchprofile.html", details)


def show_request(request):
    print("this is request page")
    return render(request, "sarpanchrequest.html", details)


def request_process(request):
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
        ins = Problem(name=username, email=email, mobile=mobile_no, role=role, von=vo_name, country=country,
                      state=state, district=city, subject=subject, detailproblem=detailprob, )
        ins.save()
        message = 'Problem Reported successfully'
        details['message'] = message
        print(details)
        return render(request, "sarpanchrequest.html", details)
    else:
        return render(request, "sarpanchrequest.html", details)


def show_notification(request):
    return render(request, "notification.html", details)


def logout(request):
    global details
    details = {}
    return render(request, "index.html")
