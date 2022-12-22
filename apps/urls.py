from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.views import ProductModelViewSet, CategoryModelViewSet, ProductImageModelViewSet, \
    ShopListCreateAPIView, ShopRetrieveAPIView

router = DefaultRouter()
router.register('product', ProductModelViewSet, 'product')
router.register('product-image', ProductImageModelViewSet, 'product_image')
# router.register('shop', ShopModelViewSet, 'shop')
router.register('category', CategoryModelViewSet, 'category')

urlpatterns = [
    path('', include(router.urls)),
    path('shop/', ShopListCreateAPIView.as_view()),
    path('shop/<str:uuid>/', ShopRetrieveAPIView.as_view()),
]
# ] + router.urls
