from django.contrib.auth.models import AbstractUser
from django.db import models

class Style(models.Model):
    style_option = models.TextField(max_length=100)

class Color(models.Model):
    color_option = models.TextField(max_length=30)

class ProductCategory(models.Model):
    name = models.TextField(max_length=100)
    priority = models.IntegerField()


# Shop class to be added

class Product(models.Model):
    name = models.TextField(max_length=100)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='static/images/product')
    # shop to be added

    def __str__(self):
        return f'{self.price} {self.product_image} {self.color.color_option}'



class Photo(models.Model):
    image = models.ImageField(upload_to='static/images/rooms')
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    description = models.TextField(max_length=50, null=True)
    products = models.ManyToManyField(Product) #somehow contains filters of the products

    def __str__(self):
        return self.description

    # Ce produse sa fie in imagine!
    # filtered_sofa = Product.objects.filter(color__product='blue', style__product='minimalist', price=2799)


class User(AbstractUser):

    def __str__(self):
        return f'{self.username} {self.email}'

class UserHistory(models.Model):
    message = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
