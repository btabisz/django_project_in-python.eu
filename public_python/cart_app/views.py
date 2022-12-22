from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from cart_app.models import Product, Category, Cart
from django.db.models import Q


@login_required
def add_product_view(request):
    cat = Category.objects.filter()
    context = {'category': cat}
    return render(request, "cart_app/add_product_form.html", context)


@login_required
def add_product(request):
    prod_name = request.POST.get('product_name', None)
    cat_id = request.POST.get('radiocat', None)

    if prod_name is "":
        messages.error(request, 'Product name not specified!')

    if cat_id is None:
        messages.add_message(request, messages.ERROR, 'Product category not selected!')

    if prod_name and cat_id is not None:
        user = request.user
        category = Category.objects.get(id=cat_id)
        prod = Product.objects.filter(Q(user_id = user.id) | Q(user_id = 1))
        for i in prod:
            if str(prod_name.upper()) == str(i.product_name.upper()):
                messages.add_message(request, messages.ERROR, 'Product: "%s" - already in the database' %prod_name)
                return redirect('/shopping-cart/add_product_view')

        formatted_name = prod_name.lower().capitalize()
        data = Product(product_name=formatted_name, category=category, user_id=user)
        data.save()
        messages.add_message(request, messages.SUCCESS, 'The product has been added!')
        return redirect('/shopping-cart/add_product_view')

    return redirect('/shopping-cart/add_product_view')


@login_required
def cart_view(request):
    prod = Cart.objects.order_by('product__category').filter(user=request.user)
    context = {'product': prod}
    return render(request, "cart_app/cart.html", context)


@login_required
def add_to_cart(request):
    product_id = request.POST.get('product', None)
    user = request.user
    products_in_cart = Cart.objects.filter(user=user)
    product = Product.objects.get(id=product_id)
    for i in products_in_cart:
        if product.id == i.product.id:
            messages.add_message(request, messages.WARNING, 'The product is already in the cart!')
            return redirect('/shopping-cart/my_search')

    data = Cart(product=product, user=user)
    data.save()
    messages.add_message(request, messages.INFO, 'The product has been added to the list!')
    return redirect('/shopping-cart/my_search')


@login_required
def my_search(request):
    user = request.user
    search_input = request.POST.get('product_name', '')
    all_products = Product.objects.filter(Q(user_id = user.id) | Q(user_id = 1)).order_by('product_name')
    cat_id = request.POST.get('radiocat', None)
    cat = Category.objects.filter()
    context = {'product': all_products, 'category': cat}
    if search_input is not '':
        context = {}
        for product in all_products:
            if str(search_input.upper()) in product.product_name.upper():
                q_set = Product.objects.filter(product_name = product.product_name).filter(Q(user_id = user.id) | Q(user_id = 1))
                context = {'product': q_set, 'category': cat}

    if search_input is '' and cat_id is not None:
        context = {}
        category = Category.objects.get(id=cat_id)
        filtered_products = Product.objects.filter(category=category).filter(Q(user_id = user.id) | Q(user_id = 1)).order_by('product_name')
        context = {'product': filtered_products, 'category': cat}

    return render(request, "cart_app/my_search_form.html", context)



@login_required
def delete_from_cart(request):
    product_id = request.POST.get('product', None)
    user = request.user
    product = Product.objects.get(id=product_id)
    data = Cart.objects.filter(product=product, user=user)
    data.delete()
    messages.add_message(request, messages.INFO, 'The product has been removed from the list!')
    return redirect('/shopping-cart/cart')

