
from django.contrib import admin
from .models import Category, ProviderInfo, Certificates, SubCategory, SendEmail, Consultant

from django.core.exceptions import ValidationError
from django import forms
from django.db.models.signals import m2m_changed

from import_export.admin import ImportExportModelAdmin

from .resources import *
from import_export import resources
# # Register your models here.

# admin.site.register(Goods)
# admin.site.register(Consultancy)
# admin.site.register(Nonconsultancy)


admin.site.register(Category)
admin.site.register(SubCategory)
# admin.site.register(ProviderInfo)
admin.site.register(Certificates)
admin.site.register(SendEmail)
admin.site.register(Consultant)
# admin.site.register(User)

# class ProviderForm(forms.ModelForm):
#     model = ProviderInfo

#     def clean(self):
#         cleaned_data = super().clean()
#         if cleaned_data.get('category').count() >= 3:
#             raise ValidationError('You can only choose 2 categories for the field Category!')


# @admin.register(ProviderInfo)
# class QuestionAdmin(admin.ModelAdmin):
#     form = ProviderForm


# def category_changed(sender, **kwargs):
#     if kwargs['instance'].category.count() > 3:
#         raise ValidationError("You can't assign more than two categories")


# m2m_changed.connect(category_changed, sender=ProviderInfo.category.through)
# from django import forms

# class ProvidersResource(resources.ModelResource):
#     category = fields.Field(
#         attribute = 'category',
#         widget = widgets.ManyToManyWidget(Category, field='category_name',seperator='|')
#     )

#     class meta:
#         model = ProviderInfo


@admin.register(ProviderInfo)
class ProviderAdmin(ImportExportModelAdmin):
    resource_class = ProvidersResource
    fields = ['category', 'no_of_categories', 'sub_categories', 'company_name', 'postal_address', 'email_address',
               'altemail_address', 'contact', 'altcontact', 'country', 'local_area', 'type_of_firm', 'date_of_registration', 'classification']
    list_display = ['get_categories', 'no_of_categories', 'get_subcategories', 'company_name', 'postal_address', 'email_address',
                    'altemail_address', 'contact', 'altcontact', 'country', 'local_area', 'type_of_firm', 'date_of_registration', 'classification']

    # def get_categories(self):
    #     return "\n".join([b.category_name for b in self.category.all()])

    # def get_subcategories(self):
    #     return "\n".join([s.sub_category_name for s in self.sub_categories.all()])


# admin.site.register(ProviderInfo, ProviderAdmin)

# Working
# @admin.register(Category)
# class CategoryAdmin(ImportExportModelAdmin):
#     resource_class = ProvidersResource
#     # fields = ['id','get_categories', 'no_of_categories', 'get_subcategories', 'company_name', 'postal_address', 'email_address',
#     #                  'altemail_address', 'contact', 'altcontact', 'country', 'local_area', 'type_of_firm', 'date_of_registration','classification']
#     list_display = ('category_name', 'category_code', 'category_description',)
