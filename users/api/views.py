'''
Views for the users API.
'''
from django.contrib.auth import get_user_model

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from users.models import LoanCustomer, LoanProvider, BankPersonnel

from users.api.serializers import UserSerializer, LoanCustomerSerializer, LoanProviderSerializer
from users.api.permissions import CreatePermissionMixin, IsLoanCustomer, IsLoanProvider



class UserViewSet(CreatePermissionMixin, viewsets.ModelViewSet):
    '''Create, Retrieve and modify information for a user.'''
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class LoanCustomerViewSet(CreatePermissionMixin, viewsets.ModelViewSet):
    '''Create, Retrieve and modify information for a loan Customer.'''
    queryset = LoanCustomer.objects.all()
    serializer_class = LoanCustomerSerializer
    permission_classes = (IsLoanCustomer,)


class LoanProviderViewSet(CreatePermissionMixin, viewsets.ModelViewSet):
    '''Create, Retrieve and modify information for a loan Provider.'''
    queryset = LoanProvider.objects.all()
    serializer_class = LoanProviderSerializer
    permission_classes = (IsLoanProvider,)
