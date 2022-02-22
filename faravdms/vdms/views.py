
from email import message
from re import sub
from urllib import request

from django.views.generic import View
import imp
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import context


# from faravdms.account.models import CustomUser

from vdms.models import ProviderInfo, Certificates, Category, SubCategory, SendEmail, Consultant
# Create your views here.

# importing form
from .forms import CategoryForm, SendEmailForm, SubCategoryForm, ProvidersForm, ConsultantForm, CertificateForm
from django.contrib import messages

from .filters import goodsFilter
from django.http import JsonResponse
from django.views.generic.edit import FormView, CreateView
from django.db import models


from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed

# EMAIL
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags

# Send Email Using EmailMessage
from django.core.mail import EmailMessage
# Login decorators to restrict views
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .resources import ProvidersResource
from tablib import Dataset
#


@login_required
def simple_upload(request):
    if request.method == 'POST':
        provider_resource = ProvidersResource()
        dataset = Dataset()
        # data = dataset.load(BOOK_DATA, format="json")
        new_provider = request.FILES['myfile']

        if not new_provider.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'upload.html')

        imported_data = dataset.load(new_provider.read(), format='xlsx')
        # result = provider_resource.import_data(imported_data, raise_errors=True, dry_run=False)
        print(imported_data)
        for data in imported_data:
            print("HELLOOOO",data[1:6])
            value = ProviderInfo(
                # data 
                id=data[0],
                # category=data[1],
                no_of_categories=data[2],
                # sub_categories=data[3],
                company_name=data[4],
                postal_address=data[5],
                email_address=data[6],
                altemail_address=data[7],
                contact=data[8],
                altcontact=data[9],
                country=data[10],
                local_area=data[11],
                type_of_firm=data[12],
                date_of_registration=data[13],
                classification=data[14],
            )
            value.save()
            # value.get_categories = data[1]
            category_id = data[1]
            category = Category.objects.get(category_name=category_id)
            value.category.add(category)
            
            sub_category_id = data[3]
            subcategory = SubCategory.objects.get(sub_category_name=sub_category_id)
            value.sub_categories.add(subcategory)
            

    return render(request, 'upload.html')


# def simple_upload(request):
#     if request.method == 'POST':
#         provider_resource = ProvidersResource()
#         dataset = Dataset()
#         new_provider = request.FILES['myfile']

#         if not new_provider.name.endswith('xlsx'):
#             messages.info(request, 'wrong format')
#             return render(request, 'upload.html')

#         imported_data = dataset.load(new_provider.read(), format='xlsx')
#         for data in imported_data:
#             # provider = Category.objects.get(category_name = data[1])
#             value = ProviderInfo(
#                 id=data[0],
#                 # category=data[1],
#                 no_of_categories=data[2],
#                 # sub_categories=data[3],
#                 company_name=data[4],
#                 postal_address=data[5],
#                 email_address=data[6],
#                 altemail_address=data[7],
#                 contact=data[8],
#                 altcontact=data[9],
#                 country=data[10],
#                 local_area=data[11],
#                 type_of_firm=data[12],
#                 date_of_registration=data[13],
#                 classification=data[14],
#                 # data[13],
#                 # data[14],
#                 # data[15],
#             )
#             # if value.save():
#             #     value.category.add(data[13])
#             #     value.sub_categories.add(data[14])

#             # value.category.add(data[1])
#             # value.sub_categories.add(data[3])
#             # value.category.set(data[1])
#             # value.objects.get(id)
#             # value.category.add(data[1])
#             value.save()

#             # value.category.add(provider)

#             value.category.add(id=data[0])
#             value.category.set(category_name=data[1])
#             value.sub_categories.set(data[3])

#     return render(request, 'upload.html')


def error_404_view(request, exception):
    return render(request, '404.html')


@login_required
def index(request):

    providers = ProviderInfo.objects.all()
    context = {'providers': providers}
    # return render(request,"index.html",{'categories':categories})
    return render(request, "index.html", context)


# -------------------(DISPLAY ALL PROVIDERS)) -------------------
@login_required
def all_providers(request):

    providers = ProviderInfo.objects.all()
    return render(request, "providers.html", {'providers': providers})


# -------------------(ADD PROVIDERS) -------------------
# def add_providers(request):
#     action = 'create'
#     form = ProvidersForm()
#     if request.method == 'POST':
#         form = ProvidersForm(request.POST)
#         if form.is_valid():
#             messages.info(request, "Successfully submitted")
#             form.save()
#             return redirect('add_providers')
#         else:
#             messages.error(request, "Something went wrong")
#             return render(request,"add_providers.html",{'form' : form})
#     else:
#         context = {'action':action,'form': form}
#         return render(request, "add_providers.html", context)
@login_required
def add_providers(request):
    if request.method == "POST":

        company_name = request.POST['companyname']
        postal_address = request.POST['postaladdress']
        email_address = request.POST['emailaddress']
        altemailaddress = request.POST['altemailaddress']
        contact = request.POST['contact']
        contact2 = request.POST['contact2']
        localarea = request.POST['localarea']
        typeoffirm = request.POST['typeoffirm']
        dateofregistration = request.POST['dateofregistration']
        classification = request.POST['classification']
        country = request.POST['country']

        no_of_categories = request.POST.get('no_of_categories', False)
        if no_of_categories == "on":
            no_of_categories = "True"

        sub_category_id = request.POST.getlist('subcategory')

        subcategory = SubCategory.objects.filter(
            sub_category_name__in=sub_category_id)

        category_id = request.POST['category']
        category = Category.objects.get(category_name=category_id)

        sub_category_id2 = request.POST.getlist('subcategory2')
        subcategory2 = SubCategory.objects.filter(
            sub_category_name__in=sub_category_id2)

        category_id2 = request.POST.get('category2', False)
        category2 = Category.objects.filter(category_name=category_id2)

        # ProviderInfo.objects.create(
        #      company_name=company_name,postal_address=postal_address, email_address=email_address, altemailaddress=altemailaddress, contact=contact, contact2=contact2, localarea=localarea, typeoffirm=typeoffirm, dateofregistration=dateofregistration, classification=classification, country=country, category=category
        # )
        providerInfo = ProviderInfo(company_name=company_name, postal_address=postal_address, email_address=email_address, altemail_address=altemailaddress, contact=contact,
                                    altcontact=contact2, local_area=localarea, type_of_firm=typeoffirm, date_of_registration=dateofregistration, classification=classification, country=country, no_of_categories=no_of_categories)
        providerInfo.save()
        providerInfo.category.add(category, *category2)
        providerInfo.sub_categories.add(*subcategory, *subcategory2)

        messages.info(request, "Successfully submitted")
        return redirect('add_providers')

    else:

        categories = Category.objects.all()

        country = ProviderInfo.COUNTRIES
        typeoffirm = ProviderInfo.TYPE_OF_FIRM
        subcategories = SubCategory.objects.all()

        providersDict = {'categories': categories, 'subcategories': subcategories,
                         'country': country, 'typeoffirm': typeoffirm, }
        return render(request,
                      "add_providers.html",
                      {
                          #   'categories':Category.objects.all(),
                          #   'subcategories':SubCategory.objects.all(),
                          #   'countries':ProviderInfo.COUNTRIES,
                          #   'typeoffirms':ProviderInfo.TYPE_OF_FIRM,
                          #   'providers':ProviderInfo.objects.all()
                          'providersDict': providersDict
                      }
                      )


# -------------------(Getting Category Values) -------------------
@login_required
def get_json_category_data(request):
    catval = list(Category.objects.values())
    return JsonResponse({'data': catval})

# -------------------(Getting SubCategory Values filterd by Category Selected) -------------------


@login_required
def get_json_subcat_data(request, *args, **kwargs):
    selected_cat = kwargs.get('category')
    obj_models = list(SubCategory.objects.filter(
        category__category_name=selected_cat).values())
    return JsonResponse({'data': obj_models})


# -------------------(UPDATE NEW) -------------------


# class UpdateCompany(View):

#     def get(self, request, pk):
#         obj = ProviderInfo.objects.get(id=pk)
#         data = list(ProviderInfo.objects.filter(id=pk).values())

#         if request.method == "POST":
#             #providerinfo = ProviderInfo.objects.get(id=kwargs)
#             id1 = request.GET.get('id', None)
#             company_name1 = request.GET.get('companyname', None)
#             postal_address1 = request.GET.get('postaladdress', None)
#             email_address1 = request.GET.get('emailaddress', None)
#             altemailaddress1 = request.GET.get('altemailaddress', None)
#             contact1 = request.GET.get('contact', None)
#             contact21 = request.GET.get('contact2', None)
#             localarea1 = request.GET.get('localarea', None)
#             typeoffirm1 = request.GET.get('typeoffirm', None)
#             dateofregistration1 = request.GET.get('dateofregistration', None)
#             classification1 = request.GET.get('classification', None)
#             country1 = request.GET.get('country', None)
#             no_of_categories1 = request.POST.get('no_of_categories', None)

#             print("hello",company_name1)
#             sub_category_id = request.GET.getlist('subcategory',None)

#             subcategory = SubCategory.objects.filter(
#                 sub_category_name__in=sub_category_id)

#             category_id = request.GET('category',None)
#             category = Category.objects.get(category_name=category_id)

#             sub_category_id2 = request.GET.getlist('subcategory2',None)
#             subcategory2 = SubCategory.objects.filter(
#                 sub_category_name__in=sub_category_id2)

#             category_id2 = request.GET.get('category2', False)
#             category2 = Category.objects.filter(category_name=category_id2)


#             obj = ProviderInfo.objects.get(id=id1)
#             obj.company_name = company_name1
#             obj.postal_address = postal_address1
#             obj.email_address = email_address1
#             obj.altemail_address = altemailaddress1
#             obj.contact = contact1
#             obj.altcontact = contact21
#             obj.local_area = localarea1
#             obj.type_of_firm = typeoffirm1
#             obj.date_of_registration = dateofregistration1
#             obj.classification = classification1
#             obj.no_of_categories = no_of_categories1
#             obj.country = country1

#             obj.save()

#             # providerinfo = {'id': obj.id, 'company_name': obj.company_name,
#             #                 'postal_address': obj.postal_address, 'email_address': obj.email_address,
#             #                 'altemail_address': obj.altemail_address, 'contact': obj.contact, 'altcontact': obj.altcontact,
#             #                 'local_area': obj.local_area, 'type_of_firm': obj.type_of_firm,
#             #                 'date_of_registration': obj.date_of_registration, 'classification': obj.classification,
#             #                 'no_of_categories': obj.no_of_categories, 'country': obj.country}

#             obj.category.add(category, *category2)
#             obj.sub_categories.add(*subcategory, *subcategory2)
#             # user = {'id': obj.id, 'name': obj.name,
#             #                 'address': obj.address, 'age': obj.age}

#             # data = {
#             #     'providerinfo': providerinfo
#             # }
#             return JsonResponse(data)
#         country = ProviderInfo.COUNTRIES
#         typeoffirm = ProviderInfo.TYPE_OF_FIRM
#         #providersDict = {'country': country, 'typeoffirm': typeoffirm, }
#         return render(request, 'update_providers.html', {"data": data, 'country': country, 'typeoffirm': typeoffirm})


# ---------------------00000000000000000000000-----------------------------------

@login_required
def UpdateCompany(request, pk):
    data = list(ProviderInfo.objects.filter(id=pk).values())
    if request.method == 'POST':
        obj = ProviderInfo.objects.get(id=pk)
        obj.company_name = request.POST['companyname']
        obj.postal_address = request.POST.get('postaladdress')
        obj.email_address = request.POST.get('emailaddress')
        obj.altemail_address = request.POST['altemailaddress']
        obj.contact = request.POST['contact']
        obj.altcontact = request.POST['contact2']
        obj.local_area = request.POST['localarea']
        obj.type_of_firm = request.POST['typeoffirm']
        obj.date_of_registration = request.POST['dateofregistration']
        obj.classification = request.POST['classification']
        obj.no_of_categories = request.POST.get('numofcat', False)
        obj.country = request.POST['country']

        sub_category_id = request.POST.getlist('subcategory')
        subcategory = SubCategory.objects.filter(
            sub_category_name__in=sub_category_id)

        category_id = request.POST['category']
        category = Category.objects.get(category_name=category_id)

        sub_category_id2 = request.POST.getlist('subcategory2')
        subcategory2 = SubCategory.objects.filter(
            sub_category_name__in=sub_category_id2)

        category_id2 = request.POST.get('category2', False)
        category2 = Category.objects.filter(category_name=category_id2)
    # if obj.is_valid():
        obj.save()
        # if category && category2
        obj.category.add(category, *category2)
        obj.sub_categories.add(*subcategory, *subcategory2)
        messages.info(request, "Successfully submitted")
        return redirect('providers')
    # else:
        # messages.error(request, "You have to choose exactly 2 categories for the field Category!")
        # return redirect('crud_ajax_update')

        # providerinfo = {'id': obj.id, 'company_name': obj.company_name,
        #                     'postal_address': obj.postal_address, 'email_address': obj.email_address,
        #                     'altemail_address': obj.altemail_address, 'contact': obj.contact, 'altcontact': obj.altcontact,
        #                     'local_area': obj.local_area, 'type_of_firm': obj.type_of_firm,
        #                     'date_of_registration': obj.date_of_registration, 'classification': obj.classification,
        #                     'no_of_categories': obj.no_of_categories, 'country': obj.country}

        # data = {
        #     'providerinfo': providerinfo
        # }
        # return redirect('providers')

    else:
        country = ProviderInfo.COUNTRIES
        typeoffirm = ProviderInfo.TYPE_OF_FIRM
        #providersDict = {'country': country, 'typeoffirm': typeoffirm, }
        return render(request, 'update_providers.html', {"data": data, 'country': country, 'typeoffirm': typeoffirm})


# ---------------------00000000000000000000000-----------------------------------
# -------------------(Get data filtered by the curent user selected NEW) -------------------

@login_required
def display_all_data(request, pk):
    obj = ProviderInfo.objects.get(id=pk)
    category_names = list(obj.category.values_list("category_name", flat=True))
    subcategory_names = list(obj.sub_categories.values_list(
        "sub_category_name", flat=True))
    countryselect = ProviderInfo.COUNTRIES
    data = {
        "id": obj.id,
        "company_name": obj.company_name,
        "postal_address": obj.postal_address,
        "email_address": obj.email_address,
        "altemail_address": obj.altemail_address,
        "contact": obj.contact,
        "altcontact": obj.altcontact,
        "local_area": obj.local_area,
        "type_of_firm": obj.type_of_firm,
        "date_of_registration": obj.date_of_registration,
        "classification": obj.classification,
        "no_of_categories": obj.no_of_categories,
        "country": obj.country,
        "category": category_names,
        "sub_categories": subcategory_names,
        "countryselect": countryselect
    }
    return JsonResponse({"data": data})


# -------------------(UPDATE VIEWS2) -------------------

# def update_provider(request, pk):
#     action = 'update'
#     providerinfo = ProviderInfo.objects.get(id=pk)
#     form = ProvidersForm(instance=providerinfo)
#     # form = ProvidersForm(request.POST or None)
#     # print('hello')
#     # print(form)

#     context = {'providerinfo':providerinfo, 'form':form}
#     return render(request, 'update_providers.html', context)

#     # if request.method == 'POST':
#     #     form = ProvidersForm(request.POST, instance=providerinfo)
#     #     if form.is_valid():
#     #         form.save()
#     #         messages.info(request, "Successfully submitted")
#     #         return redirect('providers')
#     # else:
#     #     context = {'providerinfo':providerinfo}
#     #     return render(request, 'update_providers.html', context)


# -------------------(UPDATE VIEWS) -------------------

# def update_providers(request, pk):
#     action = 'update'
#     providerinfo = ProviderInfo.objects.get(id=pk)
#     form = ProvidersForm(instance=providerinfo)

#     if request.method == 'POST':
#         form = ProvidersForm(request.POST, instance=providerinfo)
#         if form.is_valid():
#             form.save()
#             messages.info(request, "Successfully submitted")
#             return redirect('providers')

#     context = {'action': action, 'form': form}
#     return render(request, 'add_providers.html', context)


# -------------------(DELETE VIEWS) -------------------
@login_required
def delete_providers(request, pk):
    providerinfo = ProviderInfo.objects.get(id=pk)
    if request.method == "POST":
        providerinfo.delete()
        return redirect('providers')

    context = {'item': providerinfo}
    return render(request, 'delete.html', context)


# -------------------(GOODS FILTER) -------------------
@login_required
def goods_filter(request):
    providers = ProviderInfo.objects.all()
    # context = {'goods': goods}
    # subcategory in provider.sub_categories.all
    # providers = SubCategory.objects.all().filter(sub_categories__sub_category_name = "Goods")

    # providers = ProviderInfo.objects.all().filter(category__category_name = "Goods")
    # providers = ProviderInfo.objects.filter(sub_categories__category__category_name = "Goods")

    # providers = ProviderInfo.objects.filter(sub_categories__category__category_name = "Goods")
    print("Print Providers :", providers)

    myFilter = goodsFilter(request.GET, queryset=providers)
    providers = myFilter.qs
    print(myFilter.qs)
    # print("Print Providers 2 :", providers)
    context = {'providers': providers, 'myFilter': myFilter}
    # context = {'providers': providers}

    return render(request, 'goods.html', context)


@login_required
def consultant_filter(request):
    consultant = Consultant.objects.all()
    context = {'consultant': consultant}
    return render(request, 'consultants.html', context)


# -------------------(SERVICE FILTER) -------------------
@login_required
def service_filter(request):
    services = ProviderInfo.objects.all()
    context = {'services': services}
    return render(request, 'service.html', context)


# -------------------(ADD CATEGORY) -------------------
@login_required
def addCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            messages.info(request, "Successfully submitted")
            # model_instance = form.save(commit=False)
            form.save()
            return redirect('add_category')

    else:

        context = {'form': form}
        return render(request, "add_category.html", context)


# -------------------(ADD SUBCATEGORY) -------------------
@login_required
def addSubCategory(request):
    form = SubCategoryForm()
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            messages.info(request, "Successfully submitted")
            # model_instance = form.save(commit=False)
            form.save()
            return redirect('addSubCategory')

    else:

        context = {'form': form}
        return render(request, "add_subcategory.html", context)


# -------------------(ADD CERTIFICATE) -------------------
@login_required
def addCertificate(request):

    form = CertificateForm()
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            messages.info(request, "Successfully submitted")
            # model_instance = form.save(commit=False)
            introductory_letter = request.POST.get('introductory_letter')
            if introductory_letter == "on":
                introductory_letter = "True"
            form.instance.introductory_letter = introductory_letter
            form.save()
            return redirect('addCertificate')

    else:

        context = {'form': form}
        return render(request, "add_certificate.html", context)

# -------------------(SEND EMAIL) -------------------
# def sendEmail(request):
#     form = SendEmailForm()
#     current_user = request.user
#     # current_user = CustomUser
#     if request.method == 'POST':
#         form = SendEmailForm(request.POST,request.FILES)
#         print("HELLOOOOOOOOOOO", current_user.username)
#         print(form.initial)
#         print(request.POST['message'])

#         print(SendEmailForm.Meta.fields[2])
#         if form.is_valid():
#             #

#             #
#             messages.info(request, "Message Successfully Sent")
#             # form.fields['author'].initial = current_user.username
#             form.instance.author = current_user
#             form.save()
#             # model_instance = form.save(commit=False)
#             # subject = request.POST['subject']
#             # message = request.POST['message']
#             # from_mail = settings.EMAIL_HOST_USER
#             recipient_list = request.POST.getlist('receipient')
#             # fail_silently = False

#             # send_mail(
#             #     subject,
#             #     message,
#             #     from_mail,
#             #     recipient_list,
#             #     fail_silently,
#             # )
#             print("MY RECIEPIENT HELLOOOO",recipient_list)
#             send_mail(
#                 subject = request.POST['subject'],
#                 message = strip_tags(request.POST['message']),
#                 from_email = settings.EMAIL_HOST_USER,
#                 recipient_list = request.POST.getlist('receipient'),
#                 fail_silently = False
#             )

#             return redirect('tender')
#         else:
#             messages.error(request, "Message Not Sent")
#             return redirect('tender')

#     else:
#         context = {'form': form}
#         return render(request, "tender.html", context)


@login_required
def sendEmail(request):
    form = SendEmailForm()
    current_user = request.user
    # current_user = CustomUser
    if request.method == 'POST':
        form = SendEmailForm(request.POST, request.FILES)
        print("HELLOOOOOOOOOOO", current_user.username)
        print(form.initial)
        print(request.POST['message'])

        print(SendEmailForm.Meta.fields[2])
        if form.is_valid():

            messages.info(request, "Message Successfully Sent")

            file = request.FILES.get('attachment', False)
            try:
                email = EmailMessage(
                    subject=request.POST['subject'],
                    body=strip_tags(request.POST['message']),
                    from_email=settings.EMAIL_HOST_USER,
                    to=request.POST.getlist('receipient'),
                    reply_to=list(settings.EMAIL_HOST_USER),
                )
                if file:
                    for f in file:
                        email.attach(f.name, f.read(), f.content_type)
                email.send(fail_silently=False)
                form.instance.author = current_user
                form.instance.attachment = request.FILES.get(
                    'attachment', False)
                form.save()
            except:
                messages.error(request, "Message not Sent an Error Occured")
                return redirect('tender')
            return redirect('tender')

    sentmails = SendEmail.objects.all()

    context = {'form': form, 'sentmails': sentmails}
    return render(request, "tender.html", context)


# -------------------(Display Sent Emails) -------------------
@login_required
def displaySent(request):
    sentmails = SendEmail.objects.all()
    return render(request, "sent.html", {'sentmails': sentmails})


# -------------------(ADD CONSULTANT) -------------------
@login_required
def addConsultant(request):
    form = ConsultantForm()
    if request.method == 'POST':
        form = ConsultantForm(request.POST)
        if form.is_valid():
            messages.info(request, "Successfully submitted")
            # model_instance = form.save(commit=False)
            form.save()
            return redirect('add_consultant')

    else:

        context = {'form': form}
        return render(request, "add_consultant.html", context)


# -------------------(SEND INDIVIDUAL EMAILS) -------------------
@login_required
def sendIndividualEmail(request, *args):
    form = SendEmailForm()
    current_user = request.user
    # current_user = CustomUser
    if request.method == 'POST':
        form = SendEmailForm(request.POST, request.FILES)
        print("HELLOOOOOOOOOOO", current_user.username)
        print(form.initial)
        print(request.POST['message'])

        print(SendEmailForm.Meta.fields[2])
        if form.is_valid():

            messages.info(request, "Message Successfully Sent")
            file = request.FILES.get('attachment', False)
            try:
                email = EmailMessage(
                    subject=request.POST['subject'],
                    body=strip_tags(request.POST['message']),
                    from_email=settings.EMAIL_HOST_USER,
                    to=request.POST.getlist('receipient'),
                    reply_to=list(settings.EMAIL_HOST_USER),
                )
                if file:
                    for f in file:
                        email.attach(f.name, f.read(), f.content_type)
                email.send(fail_silently=False)
                form.instance.author = current_user
                form.instance.attachment = request.FILES.get(
                    'attachment', False)
                form.save()
            except:
                messages.error(request, "Message not Sent an Error Occured")
                return redirect('providers.html')
            return redirect('providers')

    providers = ProviderInfo.objects.all()
    context = {'form': form, 'providers': providers}
    return render(request, 'providers.html', context)


# -------------------(SEND To CATEGORY) -------------------
@login_required
def tenderCategory(request):
    form = SendEmailForm()
    current_user = request.user
    providers = ProviderInfo.objects.all()
    if request.method == 'POST':
        form = SendEmailForm(request.POST, request.FILES)
        print("HELLLOOOOOOO", request.POST.getlist('bcc'))
        if form.is_valid():

            messages.info(request, "Message Successfully Sent")

            file = request.FILES.getlist('attachment', False)
            try:
                email = EmailMessage(
                    subject=request.POST['subject'],
                    body=strip_tags(request.POST['message']),
                    from_email=settings.EMAIL_HOST_USER,
                    to=request.POST.getlist('receipient'),
                    cc=request.POST.getlist('cc'),
                    bcc=request.POST.getlist('bcc'),
                    reply_to=['sattakorah@faraafrica.org'],
                )

                if file:
                    for f in file:
                        email.attach(f.name, f.read(), f.content_type)
                email.send(fail_silently=False)
                form.instance.author = current_user
                form.instance.attachment = request.FILES.get(
                    'attachment', False)
                form.save()
            except:
                messages.error(request, "Message not Sent an Error Occured")
                return redirect('tender_category')
            return redirect('tender_category')

    sentmails = SendEmail.objects.all()

    context = {'form': form, 'sentmails': sentmails, 'providers': providers}
    return render(request, "tender_category.html", context)


@login_required
def getProviderEmails(request, *args, **kwargs):
    selected_cat = kwargs.get('category')
    obj_models = list(ProviderInfo.objects.filter(
        category__category_name=selected_cat).values())
    return JsonResponse({'data': obj_models})


# -------------------(SEND To SUB-CATEGORY) -------------------
@login_required
def tenderSubCategory(request):
    form = SendEmailForm()
    current_user = request.user
    providers = ProviderInfo.objects.all()
    if request.method == 'POST':
        form = SendEmailForm(request.POST, request.FILES)
        print("HELLLOOOOOOO", request.POST.getlist('bcc'))
        if form.is_valid():

            messages.info(request, "Message Successfully Sent")

            file = request.FILES.get('attachment', False)
            try:
                email = EmailMessage(
                    subject=request.POST['subject'],
                    body=strip_tags(request.POST['message']),
                    from_email=settings.EMAIL_HOST_USER,
                    to=request.POST.getlist('receipient'),
                    cc=request.POST.getlist('cc'),
                    bcc=request.POST.getlist('bcc'),
                    reply_to=['sattakorah@faraafrica.org'],
                )

                if file:
                    for f in file:
                        email.attach(f.name, f.read(), f.content_type)
                email.send(fail_silently=False)
                form.instance.author = current_user
                form.instance.attachment = request.FILES.get(
                    'attachment', False)
                form.save()
            except:
                messages.error(request, "Message not Sent an Error Occured")
                return redirect('tender_sub_category')
            return redirect('tender_sub_category')

    sentmails = SendEmail.objects.all()

    context = {'form': form, 'sentmails': sentmails, 'providers': providers}
    return render(request, "tender_subcategory.html", context)


# -------------------(GET PROVIDERS EMAIL IN SUB) -------------------
@login_required
def getProviderEmailsSub(request, *args, **kwargs):
    selected_cat = kwargs.get('subcategory')
    obj_models = list(ProviderInfo.objects.filter(
        sub_categories__sub_category_name=selected_cat).values())
    return JsonResponse({'data': obj_models})

# -------------------(SEND To Consultants) -------------------


@login_required
def tenderConsultant(request):
    form = SendEmailForm()
    current_user = request.user
    providers = ProviderInfo.objects.all()
    if request.method == 'POST':
        form = SendEmailForm(request.POST, request.FILES)
        print("HELLLOOOOOOO", request.POST.getlist('bcc'))
        if form.is_valid():

            messages.info(request, "Message Successfully Sent")

            file = request.FILES.get('attachment', False)
            try:
                email = EmailMessage(
                    subject=request.POST['subject'],
                    body=strip_tags(request.POST['message']),
                    from_email=settings.EMAIL_HOST_USER,
                    to=request.POST.getlist('receipient'),
                    cc=request.POST.getlist('cc'),
                    bcc=request.POST.getlist('bcc'),
                    reply_to=['sattakorah@faraafrica.org'],
                )

                if file:
                    for f in file:
                        email.attach(f.name, f.read(), f.content_type)
                email.send(fail_silently=False)
                form.instance.author = current_user
                form.instance.attachment = request.FILES.get(
                    'attachment', False)
                form.save()
            except:
                messages.error(request, "Message not Sent an Error Occured")
                return redirect('tender_consultant')
            return redirect('tender_consultant')

    sentmails = SendEmail.objects.all()
    consultants = Consultant.AREA_OF_SPECIALIZATION
    context = {'form': form, 'sentmails': sentmails,
               'providers': providers, 'consultants': consultants}
    return render(request, "tender_consultant.html", context)


# -------------------(GET PROVIDERS EMAIL IN SUB) -------------------
@login_required
def getConsultantEmails(request, *args, **kwargs):
    selected_cat = kwargs.get('aos')
    consultants = list(Consultant.objects.filter(
        area_of_specialization=selected_cat).values())
    # obj_models = list(ProviderInfo.objects.filter(
    #     sub_categories__sub_category_name=selected_cat).values())
    return JsonResponse({'data': consultants})
