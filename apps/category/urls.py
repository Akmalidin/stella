from django.urls import path
from .views import CategoryListCreateAPIView, CategoryDetailAPIView

urlpatterns = [
    path('', CategoryListCreateAPIView.as_view(), name='category-list-create'),  # Список и создание категорий
    path('<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),  # Операции с категорией по id
]
