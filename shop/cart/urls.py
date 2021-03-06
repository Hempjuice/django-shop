from django.urls import path

from .views import cart_add, cart_dec, cart_detail, cart_inc, cart_remove

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('inc/<int:product_id>/', cart_inc, name='cart_inc'),
    path('dec/<int:product_id>/', cart_dec, name='cart_dec'),
]
