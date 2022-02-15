from tkinter import Widget
import django_filters

from .models import *

class goodsFilter(django_filters.FilterSet):
    # sub_categories = django_filters.CharFilter(lookup_expr='icontains')
    # sub_categories = filters.ModelChoiceFilter(queryset=departments)
    class Meta:
        model = ProviderInfo
        # fields = ('postal_address')
        fields = ['sub_categories']
        