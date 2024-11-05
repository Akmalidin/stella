from rest_framework import generics, viewsets
from .models import Post, CustomerPost
from .serializers import PostSerializer, CustomerPostSerializer
from .filters import PostFilter, CustomerPostFilter

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter  # Указываем фильтр

    # При необходимости, добавьте поддержку сортировки
    ordering_fields = '__all__'  # Все поля могут быть использованы для сортировки
    ordering = ['created']  # Порядок по умолчанию



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CustomerPostListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomerPost.objects.all()
    serializer_class = CustomerPostSerializer
    filterset_class = CustomerPostFilter  # Указываем фильтр

    # При необходимости, добавьте поддержку сортировки
    ordering_fields = '__all__'  # Все поля могут быть использованы для сортировки
    ordering = ['id']  # Порядок по умолчанию

class CustomerPostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerPost.objects.all()
    serializer_class = CustomerPostSerializer