from django.db.models import Q
from django.shortcuts import render

from shop.models import Product


def search_product_view(request):
    query = request.GET.get('q')
    if query:
        lookup = Q(name__icontains=query) | Q(description__icontains=query)
        products = Product.objects.filter(lookup, stock__gt=0).distinct()
    else:
        products = Product.objects.filter(stock__gt=0)
    context = {
        'products': products
    }
    return render(request, 'shop/product/list.html', context)
