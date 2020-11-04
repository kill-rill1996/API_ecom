from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination

from core.models import Item


class PaginationItem(PageNumberPagination):
    page_size = 3
    max_page_size = 1000


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ItemFilter(filters.FilterSet):
    title = CharFilterInFilter(field_name='title', lookup_expr='in')
    category = CharFilterInFilter(field_name='category__title', lookup_expr='in')

    class Meta:
        model = Item
        fields = ['title', 'category']
