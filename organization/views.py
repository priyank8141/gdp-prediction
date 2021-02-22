import psycopg2
from django.contrib.auth.models import User
from django.shortcuts import render
from organization.models import Problem

def orguser(request):
    userdata = request.session.get('userdata')
    return render(request, "organization.html", userdata)


def orgprofile(request):
    userdata = request.session.get('userdata')
    return render(request, "organizationprofile.html", userdata)


def orgprob(request):
    userdata = request.session.get('userdata')
    data = Problem.objects.filter(role='sarpanch')
    userdata['problem'] = data
    return render(request, "orgnoti.html", userdata)

def orgdelete_data(request,id):
    userdata = request.session.get('userdata')
    data = Problem.objects.filter(role='sarpanch')
    userdata['problem'] = data
    if request.method=="POST":
        pi =Problem.objects.get(pk=id)
        pi.delete()
        return render(request, "orgnoti.html", userdata)
