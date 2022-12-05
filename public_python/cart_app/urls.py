from django.urls import path
from cart_app.views import add_product_view, cart_view, add_to_cart, my_search, delete_from_cart, add_product

urlpatterns = [
    path('add_product_view/', add_product_view, name='add_product_view'),
    path('cart/', cart_view, name='cart'),
    path('delete_from_cart/', delete_from_cart, name='delete_from_cart'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('add_product/', add_product, name='add_product'),
    path('my_search/', my_search, name='my_search'),

]