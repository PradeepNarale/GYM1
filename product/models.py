from django.db import models

# Create your models
class Product(models.Model):
    name=models.CharField(max_length=300)
    price=models.IntegerField(max_length=15)
    info=models.TextField( max_length=300)
    upload = models.ImageField(upload_to='product_images')
    links = models.URLField(max_length=200,)

    def __str__(self):
        return self.name
