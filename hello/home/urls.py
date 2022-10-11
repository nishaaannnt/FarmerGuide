from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    #here it match the word and do the task of calling views function
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("policy",views.policy,name="policy"),
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup")
]
