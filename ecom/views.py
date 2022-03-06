from os import terminal_size
from django.http.response import HttpResponseGone
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .myforms import Sellerlogin, Selsignup
from django.contrib.auth.hashers import make_password
from .models import Product, Seller, Category, Subcategory
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy

# Create your views here.

def signupsel(request):
    f=Selsignup(request.POST or None)
    if f.is_valid():        # calling the clean method of selsignup from myforms
        sel=f.save(commit=False)
        p=f.cleaned_data['password']        #f.cleaned_data.get('password')
        encp=make_password(p)
        sel.password=encp
        sel.save()
        return redirect("ecom:signin")
    return render(request,'ecom/sellerreg.html',{'form':f})

def loginseller(request):   #signseller
    f=Sellerlogin(request.POST or None)     
    if f.is_valid():
        c=f.cleaned_data.get('company')
        obj=Seller.objects.get(company=c)
        request.session['user_log']={'username':obj.name,'company':obj.company}
        return redirect('ecom:home')
    return render(request,'ecom/login.html',{'logform':f})


def logouts(request):
    request.session.pop("user_log")
    return redirect("ecom:home")

class Home(ListView):
    template_name="ecom/home.html"
    context_object_name='cat'
    # model=Category
    def get_queryset(self):
        selid=self.request.session.get("user_log")
        if selid:
            sell=Seller.objects.get(company=selid.get("company"))
            return {'cate':Category.objects.all(),
        'prod':Product.objects.filter(slid=sell)}
        else:
            return None

# def addproduct(request,pk):
#     return HttpResponseGone(str(pk))

class Addproduct(CreateView):
    template_name='ecom/addproduct.html'
    model=Product
    fields=['name','brand','desc','price','discount','image']
    context_object_name='form'
    def form_valid(self,form):
        subid=self.kwargs.get("pk")
        sub=Subcategory.objects.get(id=subid)
        selid=self.request.session.get("user_log")
        sell=Seller.objects.get(company=selid.get("company"))
        # form.instance['slid']=sell
        # form.instance['subid']=sub
        form.instance.slid=sell
        form.instance.subid=sub
        return super().form_valid(form)


class Upproduct(UpdateView):
    template_name='ecom/addproduct.html'
    model=Product
    fields=['name','brand','desc','price','discount','image']
    context_object_name='form'

class Delproduct(DeleteView):
    template_name='ecom/delproduct.html'
    model=Product
    context_object_name='prod'
    success_url=reverse_lazy('ecom:home')
    success_message='product deleted'

class Subdetail(ListView):
    template_name="ecom/subview.html"
    context_object_name='data'
    model=Subcategory
    def get_queryset(self):
        selid=self.request.session.get("user_log")
        subid=self.kwargs.get("pk")
        sub=Subcategory.objects.get(id=subid)
        if selid:
            sell=Seller.objects.get(company=selid.get("company"))
            return {'sub':sub,
        'prod':Product.objects.filter(slid=sell,subid=sub)}
        else:
            return None
        