from rest_framework import generics, viewsets, status
from .models import Post, CustomerPost, PostImage
from .serializers import PostSerializer, CustomerPostSerializer, PostImageSerializer
from .filters import PostFilter, CustomerPostFilter
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter  # Указываем фильтр
    filter_backends = [DjangoFilterBackend]
    parser_classes = [MultiPartParser, FormParser]
    # При необходимости, добавьте поддержку сортировки
    ordering_fields = '__all__'  # Все поля могут быть использованы для сортировки
    ordering = ['created']  # Порядок по умолчанию
    

class PostImageUploadView(generics.CreateAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CustomerPostListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomerPost.objects.all()
    serializer_class = CustomerPostSerializer
    filterset_class = CustomerPostFilter  # Указываем фильтр
    filter_backends = [DjangoFilterBackend]
    # При необходимости, добавьте поддержку сортировки
    ordering_fields = '__all__'  # Все поля могут быть использованы для сортировки
    ordering = ['id']  # Порядок по умолчанию

class CustomerPostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerPost.objects.all()
    serializer_class = CustomerPostSerializer