from django.contrib.auth.models import AbstractUser
from django.db import models

class Room(models.Model):
    room_option = models.CharField(max_length=20)

    def __str__(self):
        return self.room_option

class Style(models.Model):
    style_option = models.TextField(max_length=100)

    def __str__(self):
        return self.style_option


class Color(models.Model):
    color_option = models.TextField(max_length=30)

    def __str__(self):
        return self.color_option

class ProductCategory(models.Model):
    name = models.TextField(max_length=100)
    priority = models.IntegerField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.TextField(max_length=100)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='static/images/product', null=True, blank=True)

    def __str__(self):
        return f'{self.price} {self.product_image} {self.color.color_option}'

class Photo(models.Model):
    image = models.ImageField(upload_to='static/images/rooms')
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=50, null=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.description


class User(AbstractUser):
    def __str__(self):
        return f'{self.username} {self.email}'

