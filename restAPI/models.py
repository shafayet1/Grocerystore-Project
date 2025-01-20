from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Produce', 'Produce'),
    ('Dairy', 'Dairy'),
    ('Meat', 'Meat'),
    ('Snacks', 'Snacks')
) 

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    price = models.FloatField()
    quantity_in_stock = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.FloatField()