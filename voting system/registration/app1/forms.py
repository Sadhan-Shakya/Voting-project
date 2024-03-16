from django.forms import ModelForm
from django import forms

from .models import CustomUser

class AddUserForm(ModelForm):
    
    class Meta:
        model = CustomUser
        fields =('username', 'email', 'password', 'role')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'role':forms.Select(attrs={'class':'form-control'}),
        }

