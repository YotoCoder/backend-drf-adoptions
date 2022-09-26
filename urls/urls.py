from rest_framework.routers import DefaultRouter
from api.views import PetView
from user.views import UserViewSet, UserView

from django.urls import path

router = DefaultRouter()

router.register('pets', PetView, 'petview')
router.register('users', UserViewSet, 'users')

# AttributeError: type object 'UserView' has no attribute 'get_extra_actions' 

urlpatterns = router.urls

urlpatterns += [
    path('token/whoami/', UserView.as_view(), name='user'),
]

urlpatterns = router.urls