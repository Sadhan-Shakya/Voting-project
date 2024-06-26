from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from app1.emailbackend import  Emailbackend
from .models import CustomUser,Poll,PollOptions
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import AddUserForm,PollForm,PollOptionFormset,UpdateUserForm,EditUserForm
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.contrib import messages
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64


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
            # Display an error message on the login page
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

def view_profile(request):
    return render(request,'profile.html')

# @login_required(login_url='login')
def admin_dashboard(request):
    if request.user.role != 'admin':
        return HttpResponseForbidden("You are not authorized to access this page.")
    return render(request,'admin_dashboard.html')

# @login_required(login_url='login')
# def candidate_dashboard(request):
#     if request.user.role != 'candidate' and request.user.role !='admin':
#         return HttpResponseForbidden("You are not authorized to access this page.")
#     return render(request,'candidate_dashboard.html')

# @login_required(login_url='login')
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

def display_events(request):
    return render(request,'events.html')
def report_view(request):
    return render(request,'report.html')
    
class Users(View):#crud opeation ko lagi nai ho
    def get(self, request):
        UserModel_data = CustomUser.objects.all()
        return render(request, 'users.html', {'UserModeldata':UserModel_data})
    
    

class Add_UserModel(View):
    def get(self, request):
        fm = AddUserForm()
        return render(request, 'add_user.html', {'form': fm})
    
    def post(self, request):
        fm = AddUserForm(request.POST)
        if fm.is_valid():
            # Hash the password before saving
            password = fm.cleaned_data['password']
            hashed_password = make_password(password)
            fm.instance.password = hashed_password
            fm.save()
            return redirect('users')
        else:
            return render(request, 'add_user.html', {'form': fm})


# class Add_UserModel(View):
class Delete_UserModel(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        UserModeldata = CustomUser.objects.get(id=id)
        UserModeldata.delete()
        return redirect('users')

class Edit_UserModel(View):
    def get(self, request, id):
        userm = CustomUser.objects.get(id=id)
        fm = EditUserForm(instance=userm)
        return render(request, 'edit_usermodel.html', {'form':fm})
    
    def post(self, request, id):
        userm = CustomUser.objects.get(id=id)
        fm = EditUserForm(request.POST, instance=userm)
        if fm.is_valid():
            # password = fm.cleaned_data['password']
            # hashed_password = make_password(password)
            # fm.instance.password = hashed_password
            fm.save()
            return redirect('users')
        else:
            return render(request, 'edit_usermodel.html', {'form':fm})
        
class Polls(View):
    def get(self,request):
        poll_data = Poll.objects.all()
        poll_options_data = PollOptions.objects.all()

        return render(request,'events.html',{'Poll':poll_data,'Poll_options':poll_options_data})
    

def create_poll(request):
    if request.method == 'POST':
        poll_form = PollForm(request.POST)
        option_formset = PollOptionFormset(request.POST)

        if poll_form.is_valid() and option_formset.is_valid():
            poll = poll_form.save()
            options = option_formset.save(commit=False)
            for option in options:
                option.poll = poll
                option.save()
            return redirect('events')
    else:
        poll_form = PollForm()
        option_formset = PollOptionFormset()

        return render(request, 'create_poll.html', {'poll_form': poll_form, 'option_formset': option_formset})

    return render(request,'events.html',{'Poll':poll_data,'Poll_options':poll_options_data})

def profile_edit(request):
        if request.user.is_authenticated:
            current_user = CustomUser.objects.get(id=request.user.id)
            user_form=UpdateUserForm(request.POST or None, instance=current_user)

            if user_form.is_valid():
                user_form.save()
                login(request, current_user)
                messages.success(request, "User has been updated")
                return redirect('profile')
            return render(request,"profile_edit.html", {'user_form':user_form})
        else:
            messages.success(request, "you must be login ")
            return redirect('profile')

def vote(request):
    if request.method == 'POST':
        option_id = request.POST.get('option')
        print(option_id)
        if option_id:
            option = PollOptions.objects.get(id=option_id)
            # Increment the vote count for the selected option
            option.votes += 1
            option.save()

            return HttpResponse("you have voted successfully. Please check the report page for the result.")  # Redirect to a view that displays the results
    # Handle invalid form submission or GET request
    return redirect('events')
      
def delete_poll(request,poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    poll.delete()
    return redirect('events')




def report(request):
    # Retrieve poll data from the database
    poll_options = PollOptions.objects.all()

    # Convert poll data to a DataFrame
    df = pd.DataFrame(list(poll_options.values()))

    # Group poll options by poll question
    grouped_options = df.groupby('poll_id')

    # Dictionary to hold plot data for each poll question
    plot_data_dict = {}

    # Generate a bar chart for each poll question
    for poll_id, group_df in grouped_options:
        plt.figure(figsize=(8, 6))  # Set the size of the plot
        group_df.plot(kind='bar', x='option_text', y='votes', rot=45)  # Create a bar chart
        plt.xlabel('Poll Options')  # Label for the x-axis
        plt.ylabel('Vote Counts')  # Label for the y-axis
        plt.title(f'Poll Results')  # Title of the plot
        plt.tight_layout() 

        # Convert the plot to a base64-encoded string
        buffer = io.BytesIO()  # Create a memory 
        plt.savefig(buffer, format='png')  # Save the plot in PNG format to the buffer
        buffer.seek(0)  # Reset the buffer position to the start
        plot_data = base64.b64encode(buffer.read()).decode()  # Encode the plot as base64
        buffer.close()  # Close the buffer to free memory

        poll_question = Poll.objects.get(pk=poll_id).question
        # Store plot data in the dictionary
        plot_data_dict[poll_question] = plot_data

    # Pass the dictionary containing plot data for all poll questions to the template
    return render(request, 'report.html', {'plot_data_dict': plot_data_dict})
