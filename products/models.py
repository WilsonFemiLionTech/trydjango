from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField()
    description = models.CharField()
    price = models.TextField()
