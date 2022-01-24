from dataclasses import field
from pyexpat import model
from django.forms import ModelForm, Textarea, TextInput, Select
from .models import ProviderInfo, Category
from django.utils.translation import gettext_lazy as _
from django import forms

# Create the form class.


class ProvidersForm(ModelForm):
    class Meta:
        model = ProviderInfo
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    
    class Meta(object):
        model = Category
        fields = ('category_name', 'category_code', 'category_description')
        # labels = {
        #     'category_name': _('Writer'),
        # }
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
            'category_code': forms.TextInput(attrs={'class': 'form-control'}),
            'category_description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        # fields = '__all__'
