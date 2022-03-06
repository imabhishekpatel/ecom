from django.contrib import admin
from .models import Seller,Category,Subcategory,Product

# Register your models here.

admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)