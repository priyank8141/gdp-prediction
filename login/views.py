from django.shortcuts import render
# Create your views here.

def show_login(request):
    print("this is login page")
    return render(request, "login.html")
