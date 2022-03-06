from django.urls import path
from . import views
app_name='custom'
urlpatterns = [
    path("",views.Home.as_view(),name='main'),
    path("custsignup/",views.Register.as_view(),name='c-signup'),
    path("custsignin/",views.LoginPage.as_view(),name='c-signin'),
    path("custsignout/",views.signout,name='c-signout'),
    path("subcat/<int:pk>",views.Detailpage.as_view(),name='detail'),
    path("subcat/product/<int:pk>",views.Productpage.as_view(),name='prod'),
    path("subcat/product/buy/<int:pk>",views.Buy.as_view(),name='buy'),
]