from django.shortcuts import render
from django.shortcuts import render
# Create your views here.

def show_home(request):
    print("this is home page")
    return render(request, "index.html", {})
