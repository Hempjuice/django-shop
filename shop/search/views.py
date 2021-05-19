from django.db.models import Q
from django.shortcuts import render
from shop.models import Product


def search_product_view(request):
    query = request.GET.get('q')
    if query:
        lookup = Q(name__icontains=query) | Q(description__icontains=query)
        products = Product.objects.filter(lookup, available=True).distinct()
    else:
        products = Product.objects.filter(available=True)
    context = {
        'products': products
    }
    return render(request, 'shop/product/list.html', context)
