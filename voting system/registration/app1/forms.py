from django.forms import ModelForm
from django import forms

from .models import CustomUser,Poll,PollOptions

class AddUserForm(ModelForm):
    
    class Meta:
        model = CustomUser
        fields =('username', 'email', 'password', 'role')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }

class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email','role')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'role':forms.Select(attrs={'class':'form-control'})
        }
class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question']
        widgets = {
            'Question':forms.TextInput(attrs={'class':'form-control'}),
        }

PollOptionFormset = forms.inlineformset_factory(Poll, PollOptions, fields=('option_text',), extra=5, can_delete=True)

# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password', 'role']

# class UpdateUserForm(UserChangeForm):
#     email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
#     # first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
#     # last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

#     class Meta:
#         model = User
#         fields = ('username', 'email')

#     def __init__(self, *args, **kwargs):
#         super(UpdateUserForm, self).__init__(*args, **kwargs)

#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['username'].widget.attrs['placeholder'] = 'User Name'
#         self.fields['username'].label = ''
#         self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
#         self.fields['email'].help_text = '<span class="form-text text-muted"><small>Required. Enter a valid email address.</small></span>'
class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'})
        }
