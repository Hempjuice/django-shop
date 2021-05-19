from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from shop.models import Product
from .cart import Cart


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if cart.add(product=product):
        messages.success(request, 'Добавлено в корзину: ' + product.name)
    else:
        messages.error(request, 'Вы уже добавили максимальное количество')
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.error(request, 'Удалено: ' + product.name)
    return redirect('cart:cart_detail')


def cart_inc(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart:cart_detail')


def cart_dec(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.dec(product=product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
