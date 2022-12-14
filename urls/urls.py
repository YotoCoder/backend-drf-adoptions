from rest_framework.routers import DefaultRouter
from api.views import PetView, PetViewAll
from user.views import UserUpdateData, UserViewSet, UserView, UserRegister


from django.urls import path

router = DefaultRouter()

router.register('pets', PetView, 'petview')
router.register('pets-all', PetViewAll, 'pets-all')
router.register('users', UserViewSet, 'users')

urlpatterns = router.urls

urlpatterns += [
    path('token/whoami/', UserView.as_view(), name='user'),
    path('users/register', UserRegister.as_view(), name='register'),
    path('users/update', UserUpdateData.as_view(), name='update'),

]

urlpatterns = router.urls