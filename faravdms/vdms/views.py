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