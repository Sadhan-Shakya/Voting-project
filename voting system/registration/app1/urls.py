from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('profile/',views.profile)
]