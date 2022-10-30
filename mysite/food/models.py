from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(null=False, blank=False, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, blank=False, unique=False)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(null=False, blank=False, max_length=100)
    description = models.TextField(null=False, blank=False)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    cost = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to='media/products')
    created_at = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    first_name = models.CharField(null=False, blank=False,max_length=100)
    last_name = models.CharField(null=False, blank=False,max_length=100)
    phone_number = models.CharField(null=False, blank=False,max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    payment_type = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(null=False, blank=False)
    address = models.CharField(null=False, blank=False, max_length=250)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderProduct(models.Model):
    # title = models.CharField(null=False, blank=False, max_length=100)
    # description = models.TextField(null=False, blank=False)
    # category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    count = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)