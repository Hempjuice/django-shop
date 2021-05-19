from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from shop.models import Product


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            mail_body = 'Создан заказ №' + str(order.id) + '\n'
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
                mail_body += str(item['quantity']) + ' x ' + item['product'].name + '\n'
                product = get_object_or_404(Product, id=item['product'].id)
                product.stock -= item['quantity']
                if product.stock <= 0:
                    product.available = False
                product.save()
            mail_body += '\n' + 'Итого: ' + cart.get_total_amount() + ' на ' + cart.get_total_price()
            cart.clear()
            send_mail('Создан новый заказ',
                      mail_body,
                      'django-shop@gmail.com',
                      ['serdyukovma@gmail.com'], fail_silently=False)
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})
