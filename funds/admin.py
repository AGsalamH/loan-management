from django.contrib import admin
from unfold.admin import ModelAdmin as UnfoldModelAdmin

from funds.models import Fund

# Register your models here.

@admin.register(Fund)
class FundModelAdmin(UnfoldModelAdmin):
    pass
