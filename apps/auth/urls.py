from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from apps.auth.views import LoginAPI

# List of all authentication APIs.
urlpatterns = [
    path('auth/login/', LoginAPI.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]
