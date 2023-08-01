from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# create registration form
class RegistrationForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(
        attrs={'class' : 'form-control',
               'placeholder':'Enter Username'})
    )
    email=forms.EmailField(widget=forms.EmailInput(
        attrs={'class' : 'form-control',
               'placeholder':'Enter Email'})
    )
    password1=forms.CharField(widget=forms.PasswordInput(
        attrs={'class' : 'form-control',
               'placeholder':'Enter password'})
    )
    password2=forms.CharField(widget=forms.PasswordInput(
        attrs={'class' : 'form-control',
               'placeholder':'Enter confirm password'})
    )
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
      
