from dataclasses import fields
from tkinter import Widget
from import_export import resources
from .models import ProviderInfo, Category
from django import forms
# from .models import Category


class ProvidersResource(resources.ModelResource):

    class meta:
        model = ProviderInfo
        fields = ('category', 'no_of_categories', 'sub_categories', 'company_name', 'postal_address', 'email_address',
                'altemail_address', 'contact', 'altcontact', 'country', 'local_area', 'type_of_firm', 'date_of_registration','classification',)
        # exclude = ('id',)


# class ProvidersResource(resources.ModelResource):
#     # category = fields.Field(
#     #     attribute = 'category',
#     #     widget = forms.widgets.ManyToManyWidget(Category, field="category_name",seperator = '|')

#     # )
#     class meta:
#         model = ProviderInfo
#         # exclude = ('id',)
#         fields = ('category', 'no_of_categories', 'sub_categories', 'company_name', 'postal_address', 'email_address',
#                     'altemail_address', 'contact', 'altcontact', 'country', 'local_area', 'type_of_firm', 'date_of_registration','classification',)
#         # import_id_fields = ('id',)
#         # exclude = ('id',)
#         skip_unchanged = False


# WORKING
# class ProvidersResource(resources.ModelResource):
#     class meta:
#         model = Category
#         # exclude = ('id',)
#         fields = ('category_name', 'category_code', 'category_description',)
#         # import_id_fields = ('id',)
#         # exclude = ('id',)


# class ProvidersResource(resources.ModelResource):
#     class meta:
#         model = ProviderInfo

#         import_id_fields = ('id',)
#         # skip_unchanged = True
#         # report_skipped = True

#         exclude = (import_id_fields)

#         # # exclude = ('id', 'updated_date',)
#         # # skip_unchanged = True
#         # # #export_order = ('edx_id', 'edx_email')
#         # fields = ('id','get_categories', 'no_of_categories', 'get_subcategories', 'company_name', 'postal_address', 'email_address',
#         #             'altemail_address', 'contact', 'altcontact', 'country', 'local_area', 'type_of_firm', 'date_of_registration','classification')

#         # def get_import_id_fields(self):
#         #     import_id_fields = ('id',)
#         #     return self._meta.import_id_fields = import_id_fields


# class ProvidersResource(resources.ModelResource):

#     class meta:
#         model = ProviderInfo
#         import_id_fields = ("company_name",)

#         fields = ('category', 'no_of_categories', 'sub_categories', 'company_name', 'postal_address', 'email_address',
#                   'altemail_address', 'contact', 'altcontact', 'country', 'local_area', 'type_of_firm', 'date_of_registration', 'classification',)
#         widgets = {"category": {"field": "category_name"}}


# class ProvidersResource(resources.ModelResource):

#     class meta:
#         model = ProviderInfo
#         use_transactions = True
#         # import_id_fields = ("company_name",)

#         # fields = ('category', 'no_of_categories', 'sub_categories', 'company_name', 'postal_address', 'email_address',
#         #           'altemail_address', 'contact', 'altcontact', 'country', 'local_area', 'type_of_firm', 'date_of_registration', 'classification',)
#         # widgets = {"category": {"field": "category_name"}}

#         def get_categories(self, providerinfo):
#             return "\n".join([b.category_name for b in providerinfo.category.all()])
#             # collectors = ','.join(colls)
