from rest_framework import routers
from .views_api import *

router = routers.DefaultRouter()

router.register('students', StudentViewSet)
router.register('applications', ApplicationForDeducationViewSet)

urlpatterns = router.urls
