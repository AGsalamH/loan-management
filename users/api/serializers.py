from rest_framework import serializers

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from users.models import Roles

User = get_user_model()  # Return active user model.


class SignUpSerializer(serializers.ModelSerializer):
    '''Serializer for creating user objects.'''

    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('name', 'username', 'password')
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

