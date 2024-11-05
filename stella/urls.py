"""
URL configuration for stella project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication


schema_view = get_schema_view(
    openapi.Info(
        title="Stella API",
        default_version='v1',
        description="API для управления объектами недвижимости",
        contact=openapi.Contact(email="akmalmadakimov@gmail.com", name="Akmal Madakimov", url="https://wa.me/+996553565674"),
        license=openapi.License(name="Stella License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Разрешаем доступ без аутентификации для отображения Swagger
    authentication_classes=(JWTAuthentication,),

)


urlpatterns = [
    path('admin/', admin.site.urls),
    # Documentations Swagger
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),    # Swagger
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Альтернатива ReDoc
    # API urls
    path('api/category/', include('apps.category.urls')),  # Категории
    path('api/posts/', include('apps.posts.urls')),  # Посты
    path('api/users/', include('apps.users.urls')),  # Пользователи
    path('api/reviews/', include('apps.reviews.urls')),  # Отзывы
    path('api/feedback/', include('apps.feedback.urls')),  # Обратная связь
    # Auth urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Получение токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Обновление токена
    path('api/token/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),  # Выход (чёрный список токенов)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # Доступ для Медиафайлов
