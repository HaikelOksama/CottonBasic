
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to='images/product', blank=True, null=True)
    sale = models.BooleanField(default=False)
    discountedPrice = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name


class Cart(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='product')
    updated = models.DateTimeField(auto_now = True)

    def user(self):
        return self.customer.username

    def __str__(self):
        return self.customer.username
    