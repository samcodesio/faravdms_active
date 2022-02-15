from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import ProviderInfo, Category, SendEmail, SubCategory, Consultant, Certificates
from django.utils.translation import gettext_lazy as _
from django import forms
from .validators import validate_file_size


class ProvidersForm(forms.ModelForm):
    class Meta:
        model = ProviderInfo
        fields = ('category', 'sub_categories', 'company_name', 'postal_address', 'email_address', 'altemail_address',
                  'contact', 'altcontact', 'country', 'local_area', 'type_of_firm', 'date_of_registration', 'classification',)
        widgets = {
            # 'category': forms.CheckboxSelectMultiple(attrs={}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'no_of_categories': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sub_categories': forms.Select(attrs={'class': 'form-select js-example-basic-multiple', 'multiple': 'multiple'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_address': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'altemail_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'altcontact': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'local_area': forms.TextInput(attrs={'class': 'form-control'}),
            'type_of_firm': forms.Select(attrs={'class': 'form-select'}),
            'date_of_registration': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'classification': forms.TextInput(attrs={'class': 'form-control'}),
        }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['sub_categories'].queryset = SubCategory.objects.none()

#         if 'category' in self.data:
#             try:
#                 category_id = int(self.data.get('category'))
#                 self.fields['sub_categories'].queryset = SubCategory.objects.filter(category_id=category_id).order_by('sub_category_name')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk:
#             self.fields['sub_categories'].queryset = SubCategory.objects.all()


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


class SubCategoryForm(forms.ModelForm):

    class Meta(object):
        model = SubCategory
        fields = ('sub_category_name', 'category')
        widgets = {
            'sub_category_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subcategory Name'}),
            'category': forms.Select(attrs={'class': 'form-select', }),
        }
        # fields = '__all__'


class SendEmailForm(forms.ModelForm):
    attachment = forms.FileField(validators=[validate_file_size], widget=forms.FileInput(
        attrs={'class': 'form-control','multiple':'true'}), required='')
    # attachment = forms.FileField(validators=[validate_file_size])

    class Meta(object):
        model = SendEmail
        #fields = '__all__'
        fields = ('receipient', 'cc', 'bcc',
                  'subject', 'message', 'attachment')
        exclude = ['author']

        widgets = {
            'receipient': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'To:', 'required': ''}),
            'cc': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'cc:'}),
            'bcc': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Bcc:', 'required': ''}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject:'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Select(attrs={'class': 'form-control'}),
            # 'attachment': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_attachment(self, *args, **kwargs):
        attachment = self.cleaned_data.get('title')


class ConsultantForm(forms.ModelForm):

    class Meta(object):
        model = Consultant
        fields = ('first_name', 'last_name', 'area_of_specialization', 'postal_address', 'email_address',
                  'altemail_address', 'contact', 'altcontact', 'country', 'local_area')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Last Name'}),
            # 'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'area_of_specialization': forms.Select(attrs={'class': 'form-select'}),
            'postal_address': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'altemail_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'altcontact': forms.NumberInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-select'}),
            'local_area': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CertificateForm(forms.ModelForm):
    class Meta(object):
        model = Certificates
        fields = ('company_name', 'introductory_letter', 'business_registration_certificate', 'business_registration_certificate_date',
                  'certificate_to_commence_business', 'certificate_to_commence_business_date', 'valid_tax_clearance_certificate', 'valid_tax_clearance_certificate_date',
                  'valid_tax_clearance_certificate_date_expired', 'valid_vat_registration_certificate', 'valid_vat_registration_certificate_date', 'valid_ssnit_clearance_certificate',
                  'valid_ssnit_clearance_certificate_date', 'valid_ssnit_clearance_certificate_date', 'valid_ssnit_clearance_certificate_date_expired')

        widgets = {
            'company_name': forms.Select(attrs={'class': 'form-select'}),
            # 'introductory_letter': forms.RadioSelect(attrs={'class': 'form-select'}),
            'business_registration_certificate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pin Number...'}),
            'business_registration_certificate_date': forms.DateInput(attrs={'class': 'form-control','placeholder': 'Enter Issued Date dd-mm-yyyy','onfocus':"(this.type='date')"}),
            'certificate_to_commence_business': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pin Number...'}),
            'certificate_to_commence_business_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Issued Date dd-mm-yyyy','onfocus':"(this.type='date')"}),
            'valid_tax_clearance_certificate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pin Number...'}),
            'valid_tax_clearance_certificate_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Issued Date dd-mm-yyyy','onfocus':"(this.type='date')"}),
            'valid_tax_clearance_certificate_date_expired': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Expiry Date dd-mm-yyyy','onfocus':"(this.type='date')"}),
            'valid_vat_registration_certificate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pin Number...'}),
            'valid_vat_registration_certificate_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Issued Date dd-mm-yyyy','onfocus':"(this.type='date')"}),
            'valid_ssnit_clearance_certificate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pin Number...'}),
            'valid_ssnit_clearance_certificate_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Issued Date dd-mm-yyyy','onfocus':"(this.type='date')"}),
            'valid_ssnit_clearance_certificate_date_expired': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Expiry Date dd-mm-yyyy','onfocus':"(this.type='date')"}),
        }
