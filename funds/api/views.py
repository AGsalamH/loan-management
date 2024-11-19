'''
Views for the funds API.
'''
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from funds.models import Fund
from funds.api.serializers import FundSerializer

from users.api.permissions import IsLoanProvider

class FundViewSet(viewsets.ModelViewSet):
    '''Create, Retrieve and modify information for a user.'''
    serializer_class = FundSerializer
    permission_classes = (IsAuthenticated, IsLoanProvider)

    def get_queryset(self):
        return Fund.objects.all().select_related(
        'initiated_by', 'assigned_to').order_by('-created_at')
