from django.db import models
from common.models import BaseModel, StatusChoices
from django.utils.translation import gettext_lazy as _
from users.models import BankPersonnel, LoanProvider

# Create your models here.


class Fund(BaseModel):
    '''Represents a Fund.'''

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


    amount = models.DecimalField(decimal_places=2, max_digits=10, blank=True)
    interest_rate = models.DecimalField(decimal_places=2, max_digits=5, blank=True)
    max_fund_amount = models.DecimalField(decimal_places=2, max_digits=10, blank=True)
    min_fund_amount = models.DecimalField(decimal_places=2, max_digits=10, blank=True)

    duration = models.IntegerField(help_text=_('Duration in months.'))

    initiated_by = models.ForeignKey(LoanProvider, on_delete=models.CASCADE, related_name='funds')
    assigned_to = models.ForeignKey(
        BankPersonnel,
        on_delete=models.CASCADE,
        related_name='funds',
        help_text='Employee responsible for revising the Fund request.')

    status = models.CharField(_('Fund status'), choices=StatusChoices.PENDING)

    class Meta:
        ordering = ('-created_at', )
    
    def __str__(self):
        return self.name
