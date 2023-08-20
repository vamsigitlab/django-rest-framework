from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from authentication.views import SignupView, UserListView

urlpatterns = [
    path('sign-up/', SignupView.as_view(), name='sign_up'),
    path('sign-in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListView.as_view(), name='user_list'),

]