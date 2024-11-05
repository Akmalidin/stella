import django_filters
from apps.category.models import Category
from .models import Post, CustomerPost

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Фильтр по заголовку
    type_of_category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())  # Фильтр по категории
    region = django_filters.CharFilter(lookup_expr='icontains')  # Фильтр по региону
    price = django_filters.RangeFilter()  # Фильтр по диапазону цен
    created = django_filters.DateFromToRangeFilter()  # Фильтр по дате создания

    class Meta:
        model = Post
        fields = ['title', 'type_of_category', 'region', 'price', 'created']
class CustomerPostFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')  # Фильтр по имени
    region = django_filters.CharFilter(lookup_expr='icontains')  # Фильтр по региону
    type_of_category_id = django_filters.NumberFilter(field_name='type_of_category')  # Фильтр по ID категории
    price = django_filters.RangeFilter()  # Фильтр по диапазону цены

    class Meta:
        model = CustomerPost
        fields = ['name', 'region', 'type_of_category_id', 'price']
