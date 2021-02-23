
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from .models import appusers
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def show_home(request):
    print("this is home page")
    return render(request, "index.html", {})

def signupuser(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['cpassword']:
            try:
                user = User.objects.get(username=request.POST['username'])
                print("username already exist")
                return render(request,'signup.html', {'message:"username is already exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],email= request.POST['email'])
                mobile_no = request.POST['mobileno']
                gender = request.POST['gender']
                role = request.POST['role']
                vo_name = request.POST['voname']
                country = request.POST['country']
                state = request.POST['state']
                city = request.POST['city']
                newappuser = appusers(mobile=mobile_no,gender=gender,role=role,von=vo_name,country=country,state=state,district=city,user=user)
                newappuser.save()
                context = {'message': 'successful signedup'}
                return render(request, 'login.html', context)
        else:
            return render(request,'signup.html',{'error':"password doesn't match"})
    else:
        return render(request,'signup.html')

def loginuser(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            uname = request.POST['email']
            passwd = request.POST['password']
            user = authenticate(username=uname,password=passwd)
            if user is not None:
                login(request, user)
                print("loggedin")
                print(request.user.id)
                cstid=request.user.id
                cstobj = appusers.objects.get(user_id=cstid)
                print(cstobj.role)
                userdata={'id':cstid,
                          'username':request.user.username,
                          'email':request.user.email,
                          'mobile':cstobj.mobile,
                          'role':cstobj.role,
                          'von': cstobj.von,
                          'country':cstobj.country,
                          'state':cstobj.state,
                          'district':cstobj.district
                          }
                request.session['userdata'] = userdata
                # print(userdata)
                return HttpResponseRedirect('profileuser')

            else:
                print("incorect password")
                context = { 'message': 'Invalid Username & Password'}
                return render(request, 'login.html', context)
        else:
            print("login page without post")
            return render(request,'login.html')
    else:
        return HttpResponseRedirect('profileuser')


def logoutuser(request):
    request.session.flush()
    logout(request)
    print("loggedout")
    return HttpResponseRedirect('loginuser')

def profileuser(request):
    userdata=request.session.get('userdata')
    print(userdata)
    print(userdata['username'])
    if userdata['role'] == 'farmer':
        return HttpResponseRedirect('farmeruser',userdata)
    elif userdata['role'] == 'sarpanch':
        return render(request, 'sarpanch.html', userdata)
    elif userdata['role'] == 'organization':
        return HttpResponseRedirect('orguser')

