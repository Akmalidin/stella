from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'created')
        read_only_fields = ('id', 'created')
        extra_kwargs = {
            'title': {'help_text': 'Название категории'},
            'created': {'help_text': 'Дата создания категории'},
        }
