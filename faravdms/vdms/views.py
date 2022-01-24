from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from vdms.models import Goods,Consultancy,Nonconsultancy
# Create your views here.

def index(request):
    
    goods = Goods.objects.all()
    consultancy = Consultancy.objects.all()
    nonconsultancy = Nonconsultancy.objects.all()
    
    categories = {'goods':goods,'consultancy':consultancy,'nonconsultancy':nonconsultancy}
    return render(request,"index.html",{'categories':categories})


def goods(request):
    goods = Goods.objects.all()
    
    return render(request,"tables.html",{'goods':goods})


def tender(request):
    return render(request,"tender.html")

def error(request):
    return render(request,"404.html")

def add_Category(request):
    return render(request,"add_Category.html",{'add_Category':add_Category})

def add_subCategory(request):
    return render(request,"add_subCategory.html",{'add_subCategory':add_subCategory}) 

def add_Certificates(request):
    return render(request,"add_Certificates.html",{'add_Certificates':add_Certificates}) 

def add_Company(request):
    return render(request,"add_Company.html",{'add_Company':add_Company}) 

def add_Consultatnts(request):
    return render(request,"add_Consultants.html",{'add_Consultants':add_Consultatnts}) 

def add_User(request):
    return render(request,"add_User.html",{'add_User':add_User}) 