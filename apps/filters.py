from django_filters import CharFilter, NumberFilter
from django_filters.rest_framework import FilterSet

from apps.models import Product


class ProductFilter(FilterSet):
    from_price = NumberFilter(field_name='price', lookup_expr='gte')
    to_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ('from_price', 'to_price', 'category', 'shop')