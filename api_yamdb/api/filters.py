import django_filters

from reviews.models import Title


class TitleFilter(django_filters.rest_framework.FilterSet):
    genre = django_filters.CharFilter(field_name='genre__slug')
    category = django_filters.CharFilter(field_name='category__slug')
    year = django_filters.NumberFilter(field_name='year')
    name = django_filters.CharFilter(field_name='name',
                                     lookup_expr='icontains')

    class Meta:
        model = Title
        fields = ('name', 'year', 'genre', 'category')
