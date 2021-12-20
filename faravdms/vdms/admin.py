from django.contrib import admin
from .models import Consultancy, Goods, Nonconsultancy; 
# Register your models here.

admin.site.register(Goods)
admin.site.register(Consultancy)
admin.site.register(Nonconsultancy)