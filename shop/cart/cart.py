from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart and product.available:
            self.cart[product_id] = {'quantity': 1, 'price': str(product.price)}
        elif product.stock > self.cart[product_id]['quantity']:
            self.cart[product_id]['quantity'] += 1
        else:
            return False
        self.save()
        return True

    def dec(self, product):
        product_id = str(product.id)
        if self.cart[product_id]['quantity'] > 1:
            self.cart[product_id]['quantity'] -= 1
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return len(self.cart)

    def get_total_price(self):
        return '{:,}'.format(sum(item['total_price'] for item in self.cart.values())).replace(',', ' ') + " ₽"

    def get_total_amount(self):
        goods = ['товар', 'товара', 'товаров']
        amount = sum(item['quantity'] for item in self.cart.values())
        if amount % 10 == 1 and amount % 100 != 11:
            p = 0
        elif 2 <= amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
            p = 1
        else:
            p = 2
        return str(amount) + ' ' + goods[p]

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
