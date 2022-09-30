from django.db import models

# Create your models here.


class ProductModel(models.Model):
    product_name = models.CharField(max_length=128, null=False)
    product_category = models.CharField(max_length=128, null=True)
    product_price = models.IntegerField(null=False)
