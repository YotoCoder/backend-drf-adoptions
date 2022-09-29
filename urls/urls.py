from rest_framework.routers import DefaultRouter
from api.views import PetView
from user.views import UserViewSet, UserView, UserRegister


from django.urls import path

router = DefaultRouter()

router.register('pets', PetView, 'petview')
router.register('users', UserViewSet, 'users')

urlpatterns = router.urls

urlpatterns += [
    path('token/whoami/', UserView.as_view(), name='user'),
    path('users/register', UserRegister.as_view(), name='register'),
]

urlpatterns = router.urls