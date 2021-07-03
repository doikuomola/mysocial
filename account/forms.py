from django import forms
from .models import Profile

class LoginForm(forms.Form):
    """LoginForm definition."""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    
    def cleaned_password2(self):
        cd = self.cleaned_data
        if cd['passord'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match!')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')


