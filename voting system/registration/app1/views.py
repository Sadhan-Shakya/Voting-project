from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from app1.emailbackend import  Emailbackend
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import AddUserForm

from .models import UserModel

# Create your views here.
def landing_page(request):
    return render(request,'landing_page.html')

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
def voter_dashboard(request):
    return render(request,'voter_dashboard.html')

def next_page(request):
    return render(request,'next_page.html')

def profile(request):
    return render(request,'profile.html')
# def index(request):
#     return render(request,'index.html')

def users_view(request):
    return render(request,'users.html')

def analytics_view(request):
    return render(request,'analytics.html')


def report_view(request):
    return render(request,'report.html')

# class Users(View):
#     def get(self, request):
#         stu_data = Student.objects.all()
#         return render(request, 'users.html', {'studata':stu_data})
    
class Users(View):#crud opeation ko lagi nai ho
    def get(self, request):
        UserModel_data = UserModel.objects.all()
        return render(request, 'users.html', {'UserModeldata':UserModel_data})
    
# class Users(View):
#     def get(self, request):
#         Custom_User = CustomUser.objects.all()
#         return render(request, 'users.html', {'Custom_data': Custom_User})
    
class Add_UserModel(View):
    def get(self, request):
        fm = AddUserForm()
        return render(request, 'add_user.html',{'form':fm})
    
    def post(self, request):
        fm = AddUserForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('users')
        else:
            return render(request, 'add_user.html',{'form':fm})

# class Add_UserModel(View):
class Delete_UserModel(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        UserModeldata = UserModel.objects.get(id=id)
        UserModeldata.delete()
        return redirect('users')

class Edit_UserModel(View):
    def get(self, request, id):
        userm = UserModel.objects.get(id=id)
        fm = AddUserForm(instance=userm)
        return render(request, 'edit_usermodel.html', {'form':fm})
    
    def post(self, request, id):
        userm = UserModel.objects.get(id=id)
        fm = AddUserForm(request.POST, instance=userm)
        if fm.is_valid():
            fm.save()
            return redirect('users')


