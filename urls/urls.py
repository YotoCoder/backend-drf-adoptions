from rest_framework.routers import DefaultRouter
from api.views import PetView
from user.views import UserViewSet

router = DefaultRouter()

router.register('pets', PetView, 'petview')
router.register('users', UserViewSet, 'users')

urlpatterns = router.urls