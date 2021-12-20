from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('goods',views.goods,name="goods"),
    path('tender',views.tender,name="tender"),
]