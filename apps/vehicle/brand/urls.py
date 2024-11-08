from django.urls import path
from .views import BrandList, BrandDetail

urlpatterns = [
    path('', BrandList.as_view(), name='brand-list'),  # Список и создание бренда
    path('<int:pk>/', BrandDetail.as_view(), name='brand-detail'),  # Операции с брендом по id
]