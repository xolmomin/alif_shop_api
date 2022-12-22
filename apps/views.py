import itertools

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from apps.filters import ProductFilter
from apps.models import Product, Category, Shop, ProductImage
from apps.serializers import ProductModelSerializer, CategoryModelSerializer, ShopModelSerializer, \
    ProductImageModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ProductFilter
    search_fields = ['name']
    ordering_fields = ['price']
    # filterset_fields = {
    #     'price': ['gte', 'lte'],
    #     'category': ['exact'],
    #     'shop': ['exact'],
    # }


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

    def list(self, request, *args, **kwargs):
        # from model_bakery import baker
        # from faker import Faker
        # faker = Faker()
        # products = baker.make(
        #     'apps.Product',
        #     name=itertools.cycle(faker.sentences(nb=250)),
        #     # price=, #random_gen.randint(1, 100) * 100_000),  # 100_000 - 10_000_000
        #     _quantity=3000,
        #     make_m2m=True
        # )

        return super().list(request, *args, **kwargs)


class ShopListCreateAPIView(ListCreateAPIView):
    queryset = Shop.objects.all()
    parser_classes = (MultiPartParser,)
    serializer_class = ShopModelSerializer


class ShopRetrieveAPIView(RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopModelSerializer


class ProductImageModelViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageModelSerializer
