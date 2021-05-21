from django.urls import path

from .views import search_product_view

app_name = 'search'

urlpatterns = [
    path('', search_product_view, name='query'),
]
