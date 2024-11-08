from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import VehicleImage, Vehicle
from .serializers import VehicleSerializer, VehicleImageUploadSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from .filters import VehicleFilter
class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [DjangoFilterBackend]  # Укажите бэкэнд фильтра
    filterset_class = VehicleFilter  # Используйте автомобильныйфильтр
    ordering_fields = '__all__'  # Разрешить сортировку в любом поле
    ordering = ['created']  # По умолчанию по умолчанию по дате создания
class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleImageUploadView(generics.ListCreateAPIView):
    queryset = VehicleImage.objects.all()
    serializer_class = VehicleImageUploadSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)