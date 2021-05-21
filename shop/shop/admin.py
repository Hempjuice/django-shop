from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Category, Product


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 25
    list_display = ['tree_actions', 'indented_title', 'name']
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock']
    list_filter = ['price', 'stock']
    list_editable = ['price', 'stock']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
