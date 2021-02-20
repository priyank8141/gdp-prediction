import psycopg2
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