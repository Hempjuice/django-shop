from django.shortcuts import render
from django.views.generic import TemplateView

from cart.cart import Cart

from .forms import OrderCreateForm


class OrderCreate(TemplateView):
    def get(self, request, *args, **kwargs):
        form = OrderCreateForm()
        return render(request, 'orders/order/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(cart=Cart(self.request))
            return render(request, 'orders/order/created.html', {'order': order})
