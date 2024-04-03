from django.forms import ModelForm
from django import forms

from .models import CustomUser,Poll,PollOptions

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

class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question']
        widgets = {
            'Question':forms.TextInput(attrs={'class':'form-control'}),
        }

PollOptionFormset = forms.inlineformset_factory(Poll, PollOptions, fields=('option_text',), extra=5, can_delete=True)
# class PollOptionsForm(ModelForm):
#     class Meta:
#         model = PollOptions
#         fields = ['option_text']

