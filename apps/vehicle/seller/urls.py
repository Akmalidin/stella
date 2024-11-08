from django.urls import path
from .views import SellerList, SellerDetail

urlpatterns = [
    path('', SellerList.as_view(), name='seller-list-create'),
    path('<int:pk>/', SellerDetail.as_view(), name='seller-detail'),
]