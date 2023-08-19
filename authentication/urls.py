from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from authentication.views import SignupView

urlpatterns = [
    path('sign-up/', SignupView.as_view(), name='sign_up'),
    path('sign-in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]