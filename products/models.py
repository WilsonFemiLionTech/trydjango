from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField()
    description = models.CharField(max_length=15)
    price = models.TextField()
