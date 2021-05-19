from django.contrib import admin
from django.urls import path
from shop.views import (
    product_list, 
    product_detail,
)

app_name = 'shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='product_list'),
    path('catalog/<str:category_slug>/', product_list, name='product_list_by_category'),
    path('product/<str:slug>/', product_detail, name='product_detail')
]
