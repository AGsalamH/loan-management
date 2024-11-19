'''
Database Models
'''
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.hashers import make_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)

from common.models import BaseModel


# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, name, username, password, **extra_fields):
        '''
        Create and save a user with the given username and password.
        '''
        user = self.model(
            name=name,
            username=username,
            **extra_fields
        )
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(name, username, password, **extra_fields)

    def create_user(self, name, username, password, **extra_fields):
        '''
        Create normal user.
        '''

        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)

        return self._create_user(name, username, password, **extra_fields)

    def create_bank_personnel(self, name, username, password, **extra_fields):
        '''Create Bank Personnel (Allowed to access Django Admin).'''

        return self.create_superuser(name, username, password, **extra_fields)


class BaseUser(BaseModel, AbstractBaseUser):
    class Meta:
        abstract = True


class User(BaseUser, PermissionsMixin):
    '''Users are represented in the database using this model.'''
    username_validator = UnicodeUsernameValidator()

    name = models.CharField(max_length=150)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        ),
        validators=[username_validator],
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
    )

    is_active = models.BooleanField(
        _('active status'),
        default=True,
        help_text=_('Designates whether this user should be treated as active.'
        'Unselect this instead of deleting accounts.')
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

class LoanCustomer(BaseModel):
    '''Represents Loan Customer.'''

    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='loan_customer')
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    monthly_income = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.user.username


class LoanProvider(BaseModel):
    '''Represents Loan Provider.'''

    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='loan_provider')
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=120)

    def __str__(self):
       return self.user.username


class BankPersonnel(BaseModel):
    '''Represents Bank Employee.'''

    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='bank_personnel')
    bank = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)

    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
       return self.user.username

