from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('goods',views.goods,name="goods"),
    path('tender',views.tender,name="tender"),
    path('add_Category',views.add_Category,name="add_Category"),
    path('add_subCategory',views.add_subCategory,name="add_subCategory"),
    path('add_User',views.add_User,name="add_User"),
    path('add_Consultants',views.add_Consultatnts,name="add_Consultants"),
    path('add_Certificates',views.add_Certificates,name="add_Certificates"),
    path('add_Company',views.add_Company,name="add_Company"),
]