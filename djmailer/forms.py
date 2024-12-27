from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import EmailList,Subscriber,EmailCampaign

# Login Form 

class CustomAuthenticationForm(AuthenticationForm):
    username=forms.CharField(max_length=254,widget=forms.TextInput(attrs={'autofocus':True}))
    password=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'autofocus':False}))


# Registation Form 

class CustomUserCreationForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=['username','email','password1','password2']


# Add Email List Form 


class EmailListForm(forms.ModelForm):
    class Meta:
        model=EmailList
        fields=['name']

# Add Subscriber Form

class SubscriberForm(forms.ModelForm):
    class Meta:
        model=Subscriber
        fields=['email','email_list']


# Add Campaign Form

class EmailCampaignForm(forms.ModelForm):
    class Meta:
        model=EmailCampaign
        fields=['subject','content','email_list']