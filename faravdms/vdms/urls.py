from django.contrib import admin
from django.urls import path

from . import views
from .views import UpdateCompany
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name="index"),
    path('account/login/', auth_views.LoginView.as_view()),
    
    path('providers',views.all_providers,name="providers"),
    
    path('goods',views.goods_filter,name="goods"),
    path('consultants',views.consultant_filter,name="consultants"),
    path('services',views.service_filter,name="services"), 
    
    path('add_providers',views.add_providers,name="add_providers"),
    # path('update_providers/<str:pk>/',views.update_providers,name="update_providers"),
    # path('update_providers/<str:pk>/',views.update_provider,name="update_providers"), #update
    path('delete_providers/<str:pk>/',views.delete_providers,name="delete_providers"),
    path('update_providers/<str:pk>/',  views.UpdateCompany, name='crud_ajax_update'),
    # path('update_providers/<str:pk>/',  UpdateCompany.as_view(), name='crud_ajax_update'),
    
    
    path('add_certificate',views.addCertificate,name="addCertificate"),
    path('add_category',views.addCategory,name="add_category"),
    path('add_subcategory',views.addSubCategory,name="addSubCategory"),
    
    #--------------load subcategory in First CATEGORY--------------
    path('cat_json',views.get_json_category_data,name="cat_json"),
    path('subcat_json/<str:category>',views.get_json_subcat_data,name="subcat_json"),
    
    #--------------get provider emails-------------
    path('provider_email_json/<str:category>',views.getProviderEmails,name="provider_email_json"),
       #--------------get provider emails in subcategory-------------
    path('provider_emailsub_json/<str:category>/<str:subcategory>',views.getProviderEmailsSub,name="provider_emailsub_json"),
     #--------------get consultant emails-------------
    path('consultant_json/<str:aos>',views.getConsultantEmails,name="consultant_json"),
    #--------------load subcategory in Second CATEGORY--------------
    path('cat_json2',views.get_json_category_data,name="cat_json2"),
    path('subcat_json2/<str:category>',views.get_json_subcat_data,name="subcat_json2"),
    
    #--------------load subcategory in update_providers AJAX--------------
    path('update_providers/<str:pk>/<str:category>',views.get_json_subcat_data,name="subcat_json2"),
    
    path('update_providers/<str:pk>/subcat_json/<str:category>',views.get_json_subcat_data,name="subcat_json3"),
    path('update_providers/<str:pk>/subcat_json2/<str:category>',views.get_json_subcat_data,name="subcat_json3"),
   
    #--------------Display all providers--------------
    path('displaydata/<str:pk>',views.display_all_data,name="displaydata"),
    
    path('tender',views.sendEmail,name="tender"),
    
    path('sent',views.displaySent,name="sent"),
    
    path('tender_category',views.tenderCategory,name="tender_category"),
    
    path('tender_sub_category',views.tenderSubCategory,name="tender_sub_category"),
    
    path('tender_consultant',views.tenderConsultant,name="tender_consultant"),
    
    path('sendemail',views.sendIndividualEmail,name="sendemail"),
    
    path('add_consultant',views.addConsultant,name="add_consultant"),
]