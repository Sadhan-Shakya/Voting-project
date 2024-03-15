from django import forms
from .models import UserModel


class AddUserForm(forms.ModelForm):
    
    class Meta:
        model = UserModel
        fields = ("username","email","role")
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'role':forms.TextInput(attrs={'class':'form-control'}),
        }
