from rest_framework.routers import DefaultRouter
from api.views import PetTestView, PetView
from user.views import UserViewSet

router = DefaultRouter()

router.register('api/pet', PetView, 'petview')
router.register('api/test', PetTestView, 'test')
router.register('api/users', UserViewSet, 'users')

urlpatterns = router.urls