from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    stock = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)


