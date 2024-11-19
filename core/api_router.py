'''
API Viewsets Router.
'''
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views
from users.api.views import UserViewSet
from funds.api.views import FundViewSet


router = DefaultRouter()

router.register('users', UserViewSet, 'user')
router.register('funds', FundViewSet, 'fund')

app_name = 'api'
urlpatterns = router.urls

urlpatterns += [
    path('auth/', auth_views.obtain_auth_token, name='obtain-auth-token'),
]
