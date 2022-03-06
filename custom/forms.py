from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.contrib.auth import authenticate

class CReg(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    re_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
    def clean(self):
        super(CReg,self).clean()        # same as super().clean()
        p=self.cleaned_data.get('password')
        p1=self.cleaned_data.get('re_password')
        if p!=p1:
            raise forms.ValidationError('password did not match')

class Clog(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        u=self.cleaned_data.get("username")
        p=self.cleaned_data.get("password")
        val=authenticate(username=u,password=p)
        if not val:
            raise forms.ValidationError("User doesnot exist")