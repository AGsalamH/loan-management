from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from unfold.admin import ModelAdmin as UnfoldModelAdmin

from users.models import User, LoanCustomer, LoanProvider, BankPersonnel
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin, UnfoldModelAdmin):

    list_display = ('username', 'created_at')
    search_fields = ('username', 'created_at')

    list_filter = ('username', 'created_at', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('username', 'name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at')}),
    )

    # Fields displayed in the add user view
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    ordering = ('username',)
    
    readonly_fields = ('created_at', 'last_login')


@admin.register(LoanCustomer)
class LoanCustomerModelAdmin(UnfoldModelAdmin):
    pass

@admin.register(LoanProvider)
class LoanProviderModelAdmin(UnfoldModelAdmin):
    pass

@admin.register(BankPersonnel)
class BankPersonnelModelAdmin(UnfoldModelAdmin):
    pass
