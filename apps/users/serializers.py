from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())],
        label="Номер телефона"
    )
    username = serializers.CharField(
        required=False,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())],
        label="Уникальное имя пользователя для получения токена"
    )
    password = serializers.CharField(write_only=True, required=True, label="Пароль")
    password_confirm = serializers.CharField(write_only=True, required=True, label="Подтверждение пароля")

    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'phone_number', 'email', 'profile_img', 'description', 'password', 'password_confirm')

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = CustomUser.objects.create_user(**validated_data)
        return user
