'''
Views for the loans API.
'''
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from loans.models import Loan
from loans.api.serializers import LoanSerializer

from users.api.permissions import IsLoanCustomer



class LoanViewSet(viewsets.ModelViewSet):
    '''Create, Retrieve and modify information for a user.'''
    serializer_class = LoanSerializer
    permission_classes = (IsAuthenticated, IsLoanCustomer)

    def get_queryset(self):
        return Loan.objects.all().select_related(
        'requested_by', 'assigned_to').order_by('-created_at')
