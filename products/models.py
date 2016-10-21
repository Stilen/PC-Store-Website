from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    description = models.TextField()
    logo = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()
