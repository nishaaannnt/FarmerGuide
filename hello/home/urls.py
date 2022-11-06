from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    #here it match the word and do the task of calling views function
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("policy",views.policy,name="policy"),
    path("signin",views.signin,name="signin"),
    path("signup",views.signup,name="signup"),
    path("signout",views.signout,name="signout"),
    path("record",views.record,name="record"),
    path("info",views.info,name="info")
]
