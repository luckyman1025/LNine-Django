from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Company

class UserProfileForm(forms.ModelForm):


    company = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))

    profile = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))


    class Meta:
        model = UserProfile
        fields = ['company', 'profile']