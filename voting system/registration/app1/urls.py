from django.contrib import admin
from django.urls import path,include
from . import views
from .views import Users
from .views import Delete_UserModel,Edit_UserModel,Add_UserModel,create_poll,profile_edit, Polls


urlpatterns=[
    
    path('users/', Users.as_view(), name='users'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    # path('login/', views.login_view, name='login'),  # URL mapping for the login page

    path('logout/',views.LogoutPage,name='logout'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    # path('candidate_dashboard/',views.candidate_dashboard,name='candidate_dashboard'),
    path('voter_dashboard/',views.voter_dashboard,name='voter_dashboard'),
   
    path('next_page/',views.next_page,name='next_page'),
    # path('users/', views.users_view, name='users'),
    path('events/',views.display_events,name='events'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('report/', views.report, name='report'),
    path('vote/', vote, name='vote'),
# =======
#     path('report/', views.report_view, name='report'),

# >>>>>>> main
    path('add_user/', Add_UserModel.as_view(), name='add_user'),
    path('delete_usermodel/', Delete_UserModel.as_view(), name='delete_usermodel'),
    path('edit_usermodel/<int:id>/', Edit_UserModel.as_view(), name='edit_usermodel'),
    # path('index/',views.index,name='index'),
    path('create_poll/',views.create_poll, name='create_poll'),
    path('profile/', views.profile, name='profile'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    # path('display_polls/', Polls.as_view(), name='display_polls'),
    path('vote/', views.vote, name='vote'),
    path('delete_poll/<int:poll_id>/', views.delete_poll, name='delete_poll'),


    ]
