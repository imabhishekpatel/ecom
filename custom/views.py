from pyexpat import model
from unicodedata import category
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from ecom.models import Product,Category, Subcategory
from django.views import generic
from django.contrib.auth.models import User
from .forms import CReg, Clog
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

'''def home(request):
    c=Category.objects.all()
    return render(request,"custom/home.html",{'cat':c})
'''

class Home(generic.ListView):
    template_name="custom/home.html"
    context_object_name='cat'
    model=Category

class Register(generic.View):
    def get(self,request):
        return render(request,'custom/forms.html',{'form':CReg(None)})
    def post(self,request):
        f=CReg(request.POST)
        if f.is_valid():
            data=f.save(commit=False)
            p=f.cleaned_data.get('password')
            data.set_password(p)
            data.save()
            return redirect("custom:c-signin")
        return render(request,'custom/forms.html',{'form':f})

class LoginPage(generic.View):
    def get(self,request):
        return render(request,'custom/forms.html',{'form':Clog(None)})
    def post(self,request):
        f=Clog(request.POST)
        if f.is_valid():
            u=f.cleaned_data.get("username")
            p=f.cleaned_data.get("password")
            usr=authenticate(username=u,password=p)
            nxt=request.GET.get('next')
            if usr:
                login(request,usr)
            if nxt:
                return redirect(nxt)
            return redirect("custom:main")
        return render(request,'custom/forms.html',{'form':f})

def signout(request):
    logout(request)
    return redirect("custom:main")

# class Detailpage(generic.DetailView):
#     template_name="custom/detail.html"
#     model=Subcategory
#     context_object_name='data'

class Detailpage(generic.DetailView):
    template_name="custom/home.html"
    model=Subcategory
    context_object_name='sub'
    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        data['cat']=Category.objects.all()
        return data

class Productpage(generic.DetailView):
    template_name="custom/detail.html"
    model=Product
    context_object_name='prod'

class Buy(LoginRequiredMixin,generic.DetailView):
    login_url='custom:c-signin'
    template_name="custom/buy.html"
    model=Product
    context_object_name='prod'