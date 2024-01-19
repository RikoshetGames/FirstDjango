from django.contrib import admin

from catalog.models import Product, Category, Version


# Register your models here.

# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_description', 'product_price', 'in_stock', 'category',)
    list_filter = ('in_stock', 'category',)
    search_fields = ('product_name', 'product_description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name', 'category_description',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_name', 'is_active',)
    list_filter = ('is_active', 'product',)
    search_fields = ('product', 'version_name',)
