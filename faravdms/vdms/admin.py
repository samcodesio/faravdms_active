from django.contrib import admin
from .models import Category, ProviderInfo, Certificates, SubCategory, SendEmail, Consultant

from django.core.exceptions import ValidationError
from django import forms
from django.db.models.signals import m2m_changed
# # Register your models here.

# admin.site.register(Goods)
# admin.site.register(Consultancy)
# admin.site.register(Nonconsultancy)


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ProviderInfo)
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