from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    # path('candidate_dashboard/',views.candidate_dashboard,name='candidate_dashboard'),
    path('voterdashboard/',views.voterdashboard,name='voterdashboard'),
    path('profile/',views.profile,name='profile'),
    path('next_page/',views.next_page,name='next_page'),
    # path('index/',views.index,name='index'),
    
    
    

    

]
