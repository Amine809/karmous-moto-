from django.shortcuts import render

# Create your views here.
def home(reqeust):
    return render(reqeust,'pages/home.html')