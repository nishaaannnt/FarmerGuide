import http
from django.core import serializers
from multiprocessing import context
from django.shortcuts import render,redirect 
import mysql.connector as sql
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
#it describes what action to take

fname=''
lname=''
work=''
state=''
crop=''
ferti=''
cropu=''
gov=''
mob=''
def welcome(request):
    # return HttpResponse("This is about page")
    return render(request,'welcome.html')


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



def record(request):
    # return HttpResponse("This is about page")
    global state
    if request.method=='POST':
        m=sql.connect(host="localhost",user="root",passwd="6804",database="reports")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="state":

                state=value
        c=("select First_Name,work,State,Crop from farmers where State ='{}'".format(state))
        cursor.execute(c)
        i=tuple(cursor.fetchall())
        if i==():
            messages.warning(request,"No Data Available")
        else:
            context={"i":i}
            return render(request,'record.html',context)
    return render(request,'record.html')

def policy(request):
    # return HttpResponse("This is policypage")
    return render(request,'policy.html')

def signin(request):
    # return HttpResponse("This is registrationpage")
    global username,pwd
    if request.method=='POST':
        d=request.POST
        for key,value in d.items():
            if key=="username":
                username=value
            if key=="password":
                pwd=value
        user=authenticate(username=username,password=pwd)
        if user is not None:
            login(request,user)
            fname=user.first_name
            messages.success(request,'Login SuccessFul, Welcome '+fname+" !")
            return render(request,"index.html",{"fname":fname})
        else:
           
            messages.warning(request,"No valid Credentials")
    return render(request,'signin.html')

def signup(request):
    global fname,lname,s,em,pwd
    if request.method=='POST':
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fname=value
            if key=="last_name":
                lname=value
            if key=="username":
                username=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        try:
            myuser=User.objects.create_user(username,em,pwd)
            myuser.first_name=fname
            myuser.last_name=lname
        
            myuser.save()
            messages.success(request,'Account Creation SuccessFul !')
            return redirect('signin')
        except: 
            messages.error(request,"Username already taken !")
            return render(request,'signup.html')

    return render(request,'signup.html')

def info(request):
    global fname,lname,crop,work,state,ferti,cropu,gov,mob
    if request.method=='POST':
        m=sql.connect(host="localhost",user="root",passwd="6804",database="reports")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fname=value
            if key=="surname":
                lname=value
            if key=="work":
                work=value
            if key=="state":
                state=value
            if key=="crop":
                crop=value
            if key=="fertilizer":
                ferti=value
            if key=="crop_use":
                cropu=value
            if key=="gov_sub":
                gov=value
            if key=="mobile":
                mob=value
        c="insert into farmers Values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(fname,lname,work,state,crop,ferti,cropu,gov,mob)
        cursor.execute(c)
        m.commit()
        messages.success(request,"Stored successfully!")
        return render(request,'info.html')
        # reports -> farmers
    return render(request,'info.html')

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully!")
    return redirect('index')

