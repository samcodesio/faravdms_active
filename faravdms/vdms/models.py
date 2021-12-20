from django.db import models

# Create your models here.
class Goods(models.Model):
    SUB_CATEGORIES = (
        ('General Office Supplies','General Office Supplies'),
        ('Field logistics','Field logistics'),
        ('toiletries','toiletries')
    )
    COUNTRIES = (
        ('Ghana','Ghana'),
        ('Nigeria','Nigeria'),
        ('Togo','Togo')
    )
    TYPE_OF_FIRM = (
        ('Limited Liability','Limited Liability'),
        ('Partnership','Partnership'),
        ('Sole Proprietorship','Sole Proprietorship')
    )
    sub_categories = models.CharField(max_length=200,null=True,choices=SUB_CATEGORIES)
    company_name = models.TextField()
    email_address = models.EmailField(max_length = 254)
    contact = models.IntegerField
    country = models.CharField(max_length=200,null=True,choices=COUNTRIES)
    local_area = models.TextField()
    type_of_firm = models.CharField(max_length=200,null=True,choices=TYPE_OF_FIRM)
    date_of_registration = models.DateTimeField(auto_now_add=True,null=True)


class Consultancy(models.Model):
    SUB_CATEGORIES = (
        ('Management Consultancy','Management Consultancy'),
        ('Individual Consultancy','Individual Consultancy')
    )
    COUNTRIES = (
        ('Ghana','Ghana'),
        ('Nigeria','Nigeria'),
        ('Togo','Togo')
    )
    TYPE_OF_FIRM = (
        ('Limited Liability','Limited Liability'),
        ('Partnership','Partnership'),
        ('Sole Proprietorship','Sole Proprietorship')
    )
    sub_categories = models.CharField(max_length=200,null=True,choices=SUB_CATEGORIES)
    company_name = models.TextField()
    email_address = models.EmailField(max_length = 254)
    contact = models.IntegerField
    country = models.CharField(max_length=200,null=True,choices=COUNTRIES)
    local_area = models.TextField()
    type_of_firm = models.CharField(max_length=200,null=True,choices=TYPE_OF_FIRM)
    date_of_registration = models.DateTimeField(auto_now_add=True,null=True)
          



class Nonconsultancy(models.Model):
    SUB_CATEGORIES = (
        ('Security Service','Security Service'),
        ('Cleaning Service','Cleaning Service')
    )
    COUNTRIES = (
        ('Ghana','Ghana'),
        ('Nigeria','Nigeria'),
        ('Togo','Togo')
    )
    TYPE_OF_FIRM = (
        ('Limited Liability','Limited Liability'),
        ('Partnership','Partnership'),
        ('Sole Proprietorship','Sole Proprietorship')
    )
    sub_categories = models.CharField(max_length=200,null=True,choices=SUB_CATEGORIES)
    company_name = models.TextField()
    email_address = models.EmailField(max_length = 254)
    contact = models.IntegerField
    country = models.CharField(max_length=200,null=True,choices=COUNTRIES)
    local_area = models.TextField()
    type_of_firm = models.CharField(max_length=200,null=True,choices=TYPE_OF_FIRM)
    date_of_registration = models.DateTimeField(auto_now_add=True,null=True)