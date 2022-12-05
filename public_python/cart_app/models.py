from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.TextField(default = 0)

    def __str__(self):
        return f'{self.category_name}'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.TextField(default = 0, max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default = 0)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.id}: ' \
               f'{self.product_name} - ' \
               f'{self.category}' \

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f'{self.user}, {self.product}'