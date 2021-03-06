from rest_framework import viewsets, generics, filters
from favproducts.models import Client, Product, FavoriteProduct
from favproducts.serializer import ClientSerializer, ProductSerializer, FavoriteProductSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ClientsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os clientes"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ProductsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title']
    search_fields = ['title', 'brand']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class FavoriteProductsViewSet(viewsets.ModelViewSet):
    """Exibindo todas as listas de produtos favoritos de cada cliente"""
    queryset = FavoriteProduct.objects.all()
    serializer_class = FavoriteProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['client__name']
    search_fields = ['client__name']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

