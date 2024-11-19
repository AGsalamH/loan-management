from django.contrib import admin
from unfold.admin import ModelAdmin as UnfoldModelAdmin
from loans.models import Loan

# Register your models here.


@admin.register(Loan)
class LoanModelAdmin(UnfoldModelAdmin):
    pass
