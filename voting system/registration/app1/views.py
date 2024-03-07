from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from app1.emailbackend import  Emailbackend
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

# Create your views here.

def lnding_page(request):
    return render(request,'lnding_page.html')


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
                return redirect('index')
            else:
                return redirect('login')
        else:
            return HttpResponse("Username or password is incorrect")

    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
def voterdashboard(request):
    return render(request,'voterdashboard.html')

def next_page(request):
    return render(request,'next_page.html')

def profile(request):
    return render(request,'profile.html')
def index(request):
    return render(request,'index.html')

