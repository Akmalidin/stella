from django.urls import path
from .views import ReviewsView, ReviewsDetailView

urlpatterns = [
    path('', ReviewsView.as_view(), name='reviews'),
    path('<int:pk>/', ReviewsDetailView.as_view(), name='reviews-detail'),
]