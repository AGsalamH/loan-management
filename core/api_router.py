'''
API Viewsets Router.
'''
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views
from users.api.views import UserViewSet


router = DefaultRouter()

router.register('users', UserViewSet, 'user')


urlpatterns = router.urls

urlpatterns += [
    path('auth/', auth_views.obtain_auth_token, name='obtain-auth-token'),
]
