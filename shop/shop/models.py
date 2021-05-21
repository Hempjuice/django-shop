import os

from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


def get_upload_path(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return os.path.join('images/', filename)


class Category(MPTTModel):
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name='children',
                            verbose_name='Родитель'
                            )
    name = models.CharField(max_length=255, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    image = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name='Изображение')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        db_table = 'category'
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', 
        on_delete=models.CASCADE,
        verbose_name='Категория'
        )
    name = models.CharField(max_length=255, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='Остаток')
    image = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name='Изображение')

    class Meta:
        db_table = 'product'
        ordering = ('name',)
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
    
    def __str__(self):
        return self.name

    def get_price(self):
        return '{:,}'.format(self.price).replace(',', ' ') + " ₽"

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])
