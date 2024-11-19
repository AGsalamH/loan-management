from rest_framework import serializers

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from users.models import BankPersonnel, LoanCustomer, LoanProvider

User = get_user_model()  # Return active user model.


class UserSerializer(serializers.ModelSerializer):
    '''Serializer for creating user objects.'''

    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},            
        }

    def create(self, validated_data):
        '''Create and return a user with encrypted password.'''
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        '''Update an existing user.'''
        password = validated_data.pop('password')
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user

class LoanProviderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = LoanProvider
        fields = ('id', 'user', 'phone', 'address')

    def create(self, validated_data):
        user_payload = validated_data.pop('user')
        user = User.objects.create_user(**user_payload)

        return LoanProvider.objects.create(user=user, **validated_data)


class LoanCustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = LoanCustomer
        fields = ('id', 'user', 'phone', 'address')

    def create(self, validated_data):
        user_payload = validated_data.pop('user')
        user = User.objects.create_user(**user_payload)

        return LoanCustomer.objects.create(user=user, **validated_data)
