# users/views.py
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny, IsAuthenticated
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny] # Разрешить доступ без аутентификации
    parser_classes = [MultiPartParser, FormParser]
    def get(self, request):
        # Возвращаем пустую форму с названиями полей
        default_data = {
            "username": "",
            "name": "",
            "phone_number": "",
            "email": "",
            "profile_img": "",
            "description": "",
            "password": "",
            "password_confirm": ""
        }
        return Response(default_data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"success": "Пользователь успешно создан", "user_id": user.id}, status=201)
        return Response(serializer.errors, status=400)

    
class UserDetailView(generics.RetrieveDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated]  # Только для аутентифицированных пользователей

    def get_object(self):
        # Здесь можно настроить логику для получения пользователя
        return super().get_object()