import http
from multiprocessing import context
from django.shortcuts import render,HttpResponse
# Create your views here.
#it describes what action to take

def index(request):
    # to send a value to the page
    context={
        "variable":"THIS IS SENT"
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is homepage")

def about(request):
    # return HttpResponse("This is about page")
    return render(request,'about.html')

def policy(request):
    # return HttpResponse("This is policypage")
    return render(request,'policy.html')

def login(request):
    # return HttpResponse("This is registrationpage")
    return render(request,'login.html')

def signup(request):
    # return HttpResponse("This is registrationpage")
    return render(request,'signup.html')
