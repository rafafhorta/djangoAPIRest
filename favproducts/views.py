from rest_framework import viewsets, generics
from favproducts.models import Client, Product, FavoriteProduct
from favproducts.serializer import ClientSerializer, ProductSerializer, FavoriteProductSerializer, FavProductListSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ClientsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os clientes"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ProductsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class FavoriteProductsViewSet(viewsets.ModelViewSet):
    """Exibindo todas as listas de produtos favoritos de cada cliente"""
    queryset = FavoriteProduct.objects.all()
    serializer_class = FavoriteProductSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListFavProducts(generics.ListAPIView):
    """Listando os produtos favoritos"""
    def get_queryset(self):
        queryset = FavoriteProduct.objects.filter(client_id = self.kwargs['pk'])
        return queryset
    serializer_class = FavProductListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
