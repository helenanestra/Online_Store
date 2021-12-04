from django.urls import path, include
from rest_framework import routers

from .views import ProductListView, ProductUpdateView, ProductDetailView, ProductDeleteView,ProductCreateView, counter, ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('counter/', counter, name='counter'),
    path('api/', include(router.urls)),
    path('rest-api/', include('rest_framework.urls', namespace='rest_framework')),
]