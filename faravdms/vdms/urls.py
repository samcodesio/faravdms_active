from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('providers',views.providers,name="providers"),
    path('add_providers',views.add_providers,name="add_providers"),
    path('add_certificate',views.addCertificate,name="addCertificate"),
    path('add_category',views.addCategory,name="add_category"),
    path('add_subcategory',views.addSubCategory,name="addSubCategory"),
    path('add_users',views.addUsers,name="addUsers"),
    # path('tender',views.tender,name="tender"),
]