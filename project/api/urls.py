from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'posts', PostAPIViewSet, basename='post')
router.register(r'comments', CommentAPIViewSet, basename='comment')

urlpatterns = [
    path('api/register', RegisterAPIView.as_view(), name='api-register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger', SpectacularSwaggerView.as_view(), name='swagger'),
    path('api/', include(router.urls))
]