from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from app1.emailbackend import  Emailbackend
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.

def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("your password and confirm password are not same")
        else:
            my_user=CustomUser.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = Emailbackend().authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            user_role = user.role
            if user_role == 'admin':
                return redirect('admin_dashboard')
            elif user_role == 'candidate':
                return redirect('candidate_dashboard')
            elif user_role == 'voter':
                return redirect('voter_dashboard')
            else:
                return redirect('login')
        else:
            return HttpResponse("Username or password is incorrect")

    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def view_profile(request):
    return render(request,'profile.html')

@login_required(login_url='login')
def admin_dashboard(request):
    if request.user.role != 'admin':
        return HttpResponseForbidden("You are not authorized to access this page.")
    return render(request,'admin_dashboard.html')

@login_required(login_url='login')
def candidate_dashboard(request):
    if request.user.role != 'candidate':
        return HttpResponseForbidden("You are not authorized to access this page.")
    return render(request,'candidate_dashboard.html')

@login_required(login_url='login')
def voter_dashboard(request):
    if request.user.role != 'voter':
        return HttpResponseForbidden("You are not authorized to access this page.")
    return render(request,'voter_dashboard.html')