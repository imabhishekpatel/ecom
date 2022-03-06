# from os import name
from django import forms
from django.contrib.auth.hashers import check_password
# from django.db import models
# from django.forms import fields
from .models import Seller


class Selsignup(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    retype_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=Seller
        fields=['name','company','phone','email','address']
    def clean(self):
        super().clean()
        p=self.cleaned_data.get('password')
        p1=self.cleaned_data.get('retype_password')
        if p!=p1 or len(p)<6:
            raise forms.ValidationError("both password did not match, password length is smaller than 6")

class Sellerlogin(forms.Form):
    company=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        c=self.cleaned_data.get('company')
        p=self.cleaned_data.get('password')
        try:
            sel=Seller.objects.get(company=c)
        except:
            raise forms.ValidationError("user doesnot exits")
        else:
            if not check_password(p,sel.password):
                raise forms.ValidationError("password doesnot match")
    

