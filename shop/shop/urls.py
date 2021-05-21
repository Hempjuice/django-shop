from django.contrib import admin
from django.urls import path

from shop.views import MainPage, ProductDetail, ProductList

app_name = 'shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name='main_page'),
    path('catalog/<str:category_slug>/', ProductList.as_view(), name='product_list'),
    path('product/<str:slug>/', ProductDetail.as_view(), name='product_detail')
]
