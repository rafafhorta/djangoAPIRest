from django.contrib import admin
from favproducts.models import Client, Product, FavoriteProduct
# Register your models here.
class Clients(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ['name', 'email']
    list_per_page = 10

admin.site.register(Client, Clients)

class Products(admin.ModelAdmin):
    list_display = ('id', 'price', 'image', 'brand', 'title', 'reviewScore')
    list_display_links = ('id', 'title')
    search_fields = ['title', 'brand']
    list_per_page = 10

admin.site.register(Product, Products)

class FavoriteProducts(admin.ModelAdmin):
    list_display = ('id', 'client', 'product')
    list_display_links = ('id', 'client', 'product')
    search_fields = ['client']
    list_per_page = 10

admin.site.register(FavoriteProduct, FavoriteProducts)