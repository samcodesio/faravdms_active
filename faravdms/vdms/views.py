
from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse

from vdms.models import ProviderInfo, Certificates, Category, SubCategory
# Create your views here.

#importing form
from .forms import ProvidersForm,CategoryForm
from django.utils import timezone

def index(request):

    provider = ProviderInfo.objects.all()

    categories = {'provider': provider}
    # return render(request,"index.html",{'categories':categories})
    return render(request, "index.html")


def providers(request):
    
    
    return render(request, "providers.html")


def tender(request):
    return render(request, "tender.html")


def add_providers(request):
    print("hellog form is submitted")
    if request.method == "POST":
        company_name = request.POST['companyname']
        postal_address = request.POST['postaladdress']
        email_address = request.POST['emailaddress']
        altemail_address = request.POST['altemailaddress']
        contact = request.POST['contact']
        altcontact = request.POST['altcontact']
        local_area = request.POST['localarea']
        type_of_firm = request.POST['typeoffirm']
        date_of_registration = request.POST['dateofregistration']
        classification = request.POST['classification']
        country = request.POST['country']
        sub_category_id = request.POST['subcategory']
        sub_categories = SubCategory.objects.get(id=sub_category_id)
        category_id = request.POST['category']
        category = Category.objects.get(id=category_id)

        ProviderInfo.objects.create(
             company_name=company_name,postal_address=postal_address, email_address=email_address, altemail_address=altemail_address, contact=contact, altcontact=altcontact, local_area=local_area, type_of_firm=type_of_firm, date_of_registration=date_of_registration, classification=classification, country=country, category=category, sub_categories=sub_categories
        )
        # providerInfo = ProviderInfo(company_name=company_name,postal_address=postal_address, email_address=email_address, altemail_address=altemail_address, contact=contact, altcontact=altcontact, local_area=local_area, type_of_firm=type_of_firm, date_of_registration=date_of_registration, classification=classification, country=country, category=category, sub_categories=sub_categories)
        # providerInfo.save()
        
        return redirect ('add_providers')
    
    else:

        # categories = Category.objects.all()
        
        #country = ProviderInfo.COUNTRIES
        #typeoffirm = ProviderInfo.TYPE_OF_FIRM
        #subcategories = SubCategory.objects.all()
        #providersDict = {'categories':categories,'subcategories':subcategories,  'providers':providers, 'country':country, 'typeoffirm':typeoffirm, }
        return render(request, 
                      "add_providers.html",
                      {
                          'categories':Category.objects.all(),
                          'subcategories':SubCategory.objects.all(),
                          'countries':ProviderInfo.COUNTRIES,
                          'typeoffirms':ProviderInfo.TYPE_OF_FIRM,
                          }
                      )
    
    
    # categories = {'provider':provider}
    # return render(request,"index.html",{'categories':categories})
    


# add category

# def addCategory(request):
#     form = CategoryForm()
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect ('add_category')
            
#     else:
#         context = {'form':form}
#         return render(request, "add_category.html",context)

def addCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            # model_instance = form.save(commit=False)
            # model_instance.category_name = "sam"
            # model_instance.category_code = "sam"
            # model_instance.category_description = "sam"
            # model_instance.save()
            form.save()
            # form.save_m2m()
        return redirect ('add_category')
            
    else:
        context = {'form':form}
        return render(request, "add_category.html",context)

# add sub category

def addSubCategory(request):

    subcategory = SubCategory.objects.all()

    subcategories = {'subcategory': subcategory}
    # return render(request,"index.html",{'categories':categories})
    return render(request, "add-subcategory.html")


# add users
def addUsers(request):

    # subcategory = SubCategory.objects.all()

    # subcategories = {'subcategory':subcategory}
    # return render(request,"index.html",{'categories':categories})
    return render(request, "add_users.html")


def addCertificate(request):

    certificate = Certificates.objects.all()

    categories = {'provider': certificate}
    # return render(request,"index.html",{'categories':categories})
    return render(request, "add_certificate.html")


def load_subcategories(request):
    categoryId = request.get('categoryId')
    subcategory = SubCategory.objects.filter(categoryId=categoryId)
    return render(request, '',{'subcategory':subcategory})
