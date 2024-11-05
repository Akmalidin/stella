from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer

# Представление для списка категорий и добавления новой категории
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Представление для получения, обновления и удаления категории по id
class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
