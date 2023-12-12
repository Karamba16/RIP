from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

from .views_api import *

router = routers.DefaultRouter()

router.register('students', StudentViewSet, basename='students')
router.register('applications', ApplicationForDeducationViewSet, basename='applications')

urlpatterns = router.urls


urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Получение токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Обновление токена
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Проверка токена
]
