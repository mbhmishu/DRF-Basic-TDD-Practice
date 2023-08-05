from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

urlpatterns = [
    path('customer/', views.CustomerView.as_view(),name="customer"),
    path('customer/<int:pk>/', views.CustomerDetail.as_view(),name="customer-detail"),
    path('api-token-auth',auth_views.obtain_auth_token),
    path('token/',TokenObtainPairView.as_view(),name="token-obtain-pair"),
    path('token/refresh/',TokenRefreshView.as_view(),name="token-refresh"),
]
