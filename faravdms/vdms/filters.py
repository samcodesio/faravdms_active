from tkinter import Widget
import django_filters

from .models import *

class goodsFilter(django_filters.FilterSet):
    # sub_categories = django_filters.CharFilter(lookup_expr='icontains')
    # sub_categories = filters.ModelChoiceFilter(queryset=departments)
    # queryset = sub_categories__category__category_name = "Goods"a
    # sub_categories = django_filters.CharFilter(field_name='sub_categories')
    # sub_categories = django_filters.ChoiceFilter(field_name='sub_categories',lookup_expr="category__category_name='Goods'")
    
    # sub_categories = django_filters.ModelChoiceFilter(field_name='sub_categories',lookup_expr="sub_category_name",queryset=ProviderInfo.objects.filter(sub_categories__category__category_name = "Goods"))
    sub_categories = django_filters.ModelChoiceFilter(field_name='sub_categories',lookup_expr="sub_category_name",queryset=SubCategory.objects.filter(category__category_name = "Goods"))
    
    
    class Meta:
        model = ProviderInfo
        # fields = ('postal_address')
        # fields = ["sub_categories"]
        fields = '__all__'
        exclude = ['category','no_of_categories', 'company_name', 'postal_address', 'email_address', 'altemail_address',
                  'contact', 'altcontact', 'country', 'local_area', 'type_of_firm', 'date_of_registration', 'classification',]
    


# class F(django_filters.FilterSet):
#     """Filter for Books by if books are published or not"""
#     # published = BooleanFilter(field_name='published_on', method='filter_published')
#     published = ChoiceFilter

#     def filter_published(self, queryset, name, value):
#         # construct the full lookup expression.
#         lookup = '__'.join([name, 'isnull'])
#         return queryset.filter(**{lookup: False})

#         # alternatively, you could opt to hardcode the lookup. e.g.,
#         # return queryset.filter(published_on__isnull=False)

#     class Meta:
#         model = Book
#         fields = ['published']