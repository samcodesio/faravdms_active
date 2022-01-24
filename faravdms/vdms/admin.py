from django.contrib import admin
from .models import Category, ProviderInfo, Certificates, SubCategory; 
# # Register your models here.

# admin.site.register(Goods)
# admin.site.register(Consultancy)
# admin.site.register(Nonconsultancy)


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ProviderInfo)
admin.site.register(Certificates)

