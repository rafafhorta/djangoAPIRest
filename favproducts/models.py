from django.db import models

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=False, max_length=200, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='product_img')
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    reviewScore = models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return self.title

class FavoriteProduct(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, null=True)
    product = models.ManyToManyField(Product, related_name='favproduct')
    
    class Meta:
        unique_together = [['client']]