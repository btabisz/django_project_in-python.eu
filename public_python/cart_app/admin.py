from django.contrib import admin
from cart_app.models import Product

from cart_app.models import Category

from cart_app.models import Cart

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)