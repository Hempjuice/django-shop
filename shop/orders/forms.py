import os

from django import forms
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from dotenv import load_dotenv

from shop.models import Product

from .models import Order, OrderItem


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email',
                  'city', 'postal_code', 'address']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'city': 'Город',
            'postal_code': 'Индекс',
            'address': 'Адрес',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваше имя"}),
            'last_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваша фамилия"}),
            'email': forms.TextInput(attrs={"class": "form-control", "placeholder": "Адрес электронной почты"}),
            'city': forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваш город"}),
            'postal_code': forms.TextInput(attrs={"class": "form-control", "placeholder": "Индекс"}),
            'address': forms.TextInput(attrs={"class": "form-control", "placeholder": "Адрес доставки"}),
        }

    def save(self, commit=True, cart=None):
        order = super(OrderCreateForm, self).save()
        if cart:
            mail_body = 'Создан заказ №' + str(order.id) + '\n'
            for item in cart:
                product = get_object_or_404(Product, id=item['product'].id)
                if item['quantity'] < product.stock:
                    item['quantity'] = product.stock
                product.stock -= item['quantity']
                product.save()
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
                mail_body += str(item['quantity']) + ' x ' + item['product'].name + '\n'
            mail_body += '\n' + 'Итого: ' + cart.get_total_amount() + ' на ' + cart.get_total_price()
            cart.clear()
            load_dotenv()
            send_mail('Создан новый заказ',
                      mail_body,
                      [os.getenv('SHOP_EMAIL')],
                      order.email,
                      fail_silently=False)
        return order
