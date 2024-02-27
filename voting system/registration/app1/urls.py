from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('signup/',views.SignupPage,name='signup'),
    path("detail", views.detail,name="detail"),
    path("result", views.result,name="result"),
    path("index", views.index,name="index"),
    path('login/',views.LoginPage,name='login'),
    path('profile/',views.profile,name='profile'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('candidate_dashboard/',views.candidate_dashboard,name='candidate_dashboard'),
    path('voter_dashboard/',views.voter_dashboard,name='voter_dashboard'),
]