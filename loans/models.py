from django.db import models
from common.models import BaseModel, StatusChoices
from django.utils.translation import gettext_lazy as _
from users.models import BankPersonnel, LoanCustomer

# Create your models here.


class Loan(BaseModel):
    '''Represents loans database table.'''

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    amount = models.DecimalField(decimal_places=2, max_digits=10, blank=True)
    interest_rate = models.DecimalField(decimal_places=2, max_digits=5, blank=True)
    max_loan_amount = models.DecimalField(decimal_places=2, max_digits=10, blank=True)
    min_loan_amount = models.DecimalField(decimal_places=2, max_digits=10, blank=True)

    duration = models.IntegerField(help_text=_('Duration in months.'), blank=True)

    status = models.CharField(_('Loan status'), choices=StatusChoices.choices, default=StatusChoices.PENDING)

    requested_by = models.ForeignKey(LoanCustomer, on_delete=models.CASCADE, related_name='loans')
    assigned_to = models.ForeignKey(
        BankPersonnel,
        on_delete=models.CASCADE,
        related_name='loans',
        help_text='Employee responsible for revising the Loan request.')

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name
