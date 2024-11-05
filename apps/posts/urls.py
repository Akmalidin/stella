from django.urls import path, include
from .views import PostList, PostDetail, CustomerPostListCreateAPIView, CustomerPostDetailAPIView

urlpatterns = [
    path('', PostList.as_view(), name='post-list-create'),  # Список и создание постов
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),  # Операции с постом по id
    path('customer/', CustomerPostListCreateAPIView.as_view(), name='customer-post-list-create'),  # Список и создание клиентских постов
    path('customer/<int:pk>/', CustomerPostDetailAPIView.as_view(), name='customer-post-detail'),  # Операции с клиентским постом по id
]