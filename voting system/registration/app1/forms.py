from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser, Poll, PollOptions
from django.contrib.auth.models import User


class AddUserForm(ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'role')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'username': '',  # Remove the help text
        }
    

class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question']
        widgets = {
            'Question': forms.TextInput(attrs={'class': 'form-control'}),  # Should be 'question' instead of 'Question'
        }

PollOptionFormset = forms.inlineformset_factory(Poll, PollOptions, fields=('option_text',), extra=5, can_delete=True)

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']

class UpdateUserForm(UserChangeForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))

    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text =  '<span class="form-text text-muted"><small>Enter your user name.</small></span>'
        self.fields['email'].help_text = '<span class="form-text text-muted"><small>Required. Enter a valid email address.</small></span>'
        
        self.fields.pop('password', None)
