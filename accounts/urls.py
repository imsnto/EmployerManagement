from django.contrib.auth.views import LoginView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import index, UserRegistrationView, UserLoginAPIView, UserProfileView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('auth/login/', UserLoginAPIView.as_view() , name='login'),
    path('auth/signup/', UserRegistrationView.as_view(), name='signup'),
    path('auth/profile/', UserProfileView.as_view(), name='index'),
]

