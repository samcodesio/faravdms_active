from django.contrib import admin
from .models import CustomUser

from .forms import CreateUserForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CreateUserForm
    
    fieldsets = (
        *UserAdmin.fieldsets,(
            'Role',{
                'fields':(
                    'role',
                )
            }
        )
    )
    
admin.site.register(CustomUser,CustomUserAdmin)