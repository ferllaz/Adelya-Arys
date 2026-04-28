from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, blank=True) # Новое поле
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    def __str__(self):
        return self.title