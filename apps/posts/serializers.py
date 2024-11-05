from rest_framework import serializers
from apps.category.models import Category
from .models import Post, CustomerPost


class PostSerializer(serializers.ModelSerializer):
    type_of_category = serializers.CharField(source='type_of_category.title', read_only=True, label='Категория')
    type_of_category_id = serializers.PrimaryKeyRelatedField(
            source='type_of_category',  # Указываем, что это связано с полем type_of_category
            queryset=Category.objects.all(),  # Указываем, что можем выбрать из всех категорий
            write_only=True,  # Делаем его доступным только для записи
            label='Категория'  # Можно также добавить метку для идентификатора категории
        )
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'type_of_category',
            'type_of_category_id',
            'image',
            'complete',
            'address',
            'region',
            'rooms',
            'area',
            'floor',
            'price',
            'description',
            'created',
            'updated'
        )
        extra_kwargs = {
            'title': {'help_text': 'Название объекта недвижимости'},
            'image': {'help_text': 'Изображение'},
            'complete': {'help_text': 'Завершено'},
            'address': {'help_text': 'Адрес'},
            'region': {'help_text': 'Регион'},
            'rooms': {'help_text': 'Количество комнат'},
            'area': {'help_text': 'Площадь'},
            'floor': {'help_text': 'Этаж'},
            'price': {'help_text': 'Цена в $'},
            'description': {'help_text': 'Описание'},
        }

class CustomerPostSerializer(serializers.ModelSerializer):
    type_of_category = serializers.CharField(source='type_of_category.title', read_only=True, label='Категория')
    type_of_category_id = serializers.PrimaryKeyRelatedField(
            source='type_of_category',  # Указываем, что это связано с полем type_of_category
            queryset=Category.objects.all(),  # Указываем, что можем выбрать из всех категорий
            write_only=True,  # Делаем его доступным только для записи
            label='Категория'  # Можно также добавить метку для идентификатора категории
        )
    class Meta:
        model = CustomerPost
        fields = (
            'id',
            'name',
            'type_of_category',
            'type_of_category_id',
            'region',
            'rooms',
            'price',
            'phone_number'
        )
        extra_kwargs = {
            'name': {'help_text': 'Название объекта недвижимости'},
            'region': {'help_text': 'Район расположения'},
            'rooms': {'help_text': 'Количество комнат'},
            'price': {'help_text': 'Стоимость недвижимости'},
            'phone_number': {'help_text': 'Контактный номер'},
        }
    