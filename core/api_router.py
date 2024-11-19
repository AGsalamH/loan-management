'''
API Viewsets Router.
'''
from rest_framework.routers import DefaultRouter
from users.api.views import UserViewSet


router = DefaultRouter()

router.register('users', UserViewSet, 'user')


urlpatterns = router.urls
