from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView

from .models import Category, Product


class MainPage(TemplateView):
    template_name = 'shop/main.html'


class ProductList(ListView):
    def get(self, request, *args, **kwargs):
        category_slug = self.kwargs.get('category_slug')
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, stock__gt=0)
        context = {
            'category': category,
            'products': products
        }
        return render(request, 'shop/product/list.html', context)


class ProductDetail(DetailView):
    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug, stock__gt=0)
        context = {
            'path': product.category.get_ancestors(include_self=True),
            'product': product
        }
        return render(request, 'shop/product/detail.html', context)
