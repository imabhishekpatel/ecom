from django.urls import path
from . import views
app_name='ecom'

urlpatterns = [
    path('', views.Home.as_view(),name='home'),
    path('register/', views.signupsel,name='signup'),
    path('login/', views.loginseller,name='signin'),
    path('logout/', views.logouts,name='signout'),
    # path('prooduct/<int:pk>', views.addproduct,name='addproduct'),
    path('product/<int:pk>', views.Addproduct.as_view(),name='addproduct'),
    path('product/update/<int:pk>', views.Upproduct.as_view(),name='upproduct'),
    path('product/delete/<int:pk>', views.Delproduct.as_view(),name='delproduct'),
    path('product/showdetail/<int:pk>', views.Subdetail.as_view(),name='product'),
    
    

]