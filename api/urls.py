from rest_framework.routers import DefaultRouter
from .views import PetTestView, PetView

router = DefaultRouter()

router.register('api/pets', PetView, 'petview')
router.register('api/test', PetTestView, 'test')

urlpatterns = router.urls