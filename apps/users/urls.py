# users/urls.py
from django.urls import path
from .views import UserRegistrationView, UserDetailView

urlpatterns = [
    path('', UserRegistrationView.as_view(), name='register'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
