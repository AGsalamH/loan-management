"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from os import environ
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-clld(0*!mt*a!i%wvqk)z^nb)&-ml1e-t0@&r1i&%9as$@k3a='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = [
    'unfold',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'drf_spectacular',
]

LOCAL_APPS = [
    'common',
    'users',
    'funds',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('DB_NAME'),
        'USER': environ.get('DB_USER'),
        'PASSWORD': environ.get('DB_PASSWORD'),
        'HOST': environ.get('DB_HOST'),
        'PORT': environ.get('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



AUTH_USER_MODEL = 'users.User'


# REST_FRAMEWORK 
# -----------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema', # Generate Schema openapi specification.
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}


# UNFOLD
# ------------------------------------------------------------------------------
UNFOLD = {
    'SITE_TITLE': 'Loan Management',
    'SITE_HEADER': 'Loan Management Admin',

    'SITE_SYMBOL': 'admin_panel_settings',  # symbol from icon set
    'SHOW_HISTORY': True, # show/hide 'History' button, default: True
    'SHOW_VIEW_ON_SITE': True, # show/hide 'View on site' button, default: True
    'SIDEBAR': {
        'show_search': False,  # Search in applications and models names
        'show_all_applications': False,  # Dropdown with all applications and models
        'navigation': [
            {
                'title': _('Navigation'),
                'separator': False,  # Top border
                'collapsible': True,  # Collapsible group of links
                'items': [
                    {
                        'title': _('Dashboard'),
                        'icon': 'dashboard',  # Supported icon set: https://fonts.google.com/icons
                        'link': reverse_lazy('admin:index'),
                        # 'badge': 'sample_app.badge_callback',
                        'permission': lambda request: request.user.is_superuser,
                    },
                    {
                        'title': _('Users'),
                        'icon': 'people',
                        'link': reverse_lazy('admin:users_user_changelist'),
                    },
                ],
            },
        ],
    },
}
