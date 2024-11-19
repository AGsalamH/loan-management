'''
Views for the users API.
'''
from django.contrib.auth import get_user_model

from rest_framework import generics, viewsets

from users.api.serializers import SignUpSerializer
from users.api.permissions import RegisterOrIsAuthenticated



class UserViewSet(viewsets.ModelViewSet):
    '''Create, Retrieve and modify information for a user.'''
    queryset = get_user_model().objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (RegisterOrIsAuthenticated,)
