from django import forms
from.models import *
from django.contrib.auth.forms import AuthenticationForm

class empform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=employee
        fields=['name','age','designation','salary','emailid','password']
class emplogin(AuthenticationForm):
    username=forms.EmailField(label='emailid')

class product(forms.ModelForm):
    class Meta:
        model=details
        fields='__all__'