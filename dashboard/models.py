from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Produce', 'Produce'),
    ('Dairy', 'Dairy'),
    ('Meat', 'Meat'),
    ('Snacks', 'Snacks')
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name}'
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)
    staff = models.ForeignKey(User, models.CASCADE, null = True)
    order_quantity = models.PositiveSmallIntegerField(null=True)
    date = models.DateTimeField(auto_now_add = True)


    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'

