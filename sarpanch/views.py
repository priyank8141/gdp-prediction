import psycopg2
from django.http import HttpResponseRedirect
from django.shortcuts import render
from farmer.views import search_weather
from home.decorator import role_required
from organization.models import Problem

# Create your views here.


@role_required(allowed_roles =["sarpanch"])
def sarpanchuser(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
        userdata = request.session.get('userdata')
        co=userdata['country']
        st= userdata['state']
        di= userdata['district']
        # search_weather(co,st,di)
        return render(request, "sarpanch.html", userdata)


@role_required(allowed_roles =["sarpanch"])
def sarpanchprofile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
        userdata = request.session.get('userdata')
        return render(request, "sarpanchprofile.html", userdata)



@role_required(allowed_roles =["sarpanch"])
def sarpanchreport(request):
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
                return render(request, "sarpanchrequest.html", userdata)
        else:
                return render(request, "sarpanchrequest.html", userdata)



@role_required(allowed_roles =["sarpanch"])
def sapredict(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
        userdata = request.session.get('userdata')
        if (request.method == 'POST'):
            co = request.POST['country']
            st = request.POST['state']
            ci = request.POST['city']
            search_weather(co, st, ci)
        return render(request, "sarpanch.html",userdata)


@role_required(allowed_roles =["sarpanch"])
def sarpanchprob(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
        userdata = request.session.get('userdata')
        city = userdata['district']
        print(city)
        data = Problem.objects.filter(role='farmer', district=city)
        userdata['problem'] = data
        return render(request, "notification.html", userdata)


@role_required(allowed_roles =["sarpanch"])
def sardelete_data(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('loginuser')
    else:
        userdata = request.session.get('userdata')
        data = Problem.objects.filter(role='farmer')
        userdata['problem'] = data
        if request.method=="POST":
            pi =Problem.objects.get(pk=id)
            pi.delete()
            return render(request, "notification.html", userdata)
