from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
from rest_framework import serializers



def upload_image(instance, filename):
    return f'{instance}-{filename}'


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    username = models.CharField(max_length=100, unique=True)
    picture = models.ImageField(upload_to=upload_image, blank=True, null=True)

    def __str__(self):
        return self.username


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=1000, unique=True)
    picture = models.ImageField(upload_to=upload_image, blank=True, null=True)
    link = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=False, related_name='restaurant_product')
    name = models.CharField(max_length=1000)
    detail = models.CharField(max_length=1000)
    price = models.CharField(max_length=100)
    picture = models.ImageField(upload_to=upload_image, blank=True, null=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=False, related_name='rating_product')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=False, related_name='rating_profile')
    product_rate = models.IntegerField(blank=True, null=True)
    size = models.IntegerField()
    complement = models.IntegerField()
    side_dish = models.IntegerField()
    comment = models.CharField(max_length=9999)


class Wishlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=False, related_name='wishlist_profile')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=False, related_name='wishlist_product')
    note = models.CharField(max_length=9999)