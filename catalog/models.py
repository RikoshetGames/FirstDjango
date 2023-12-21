from django.db import models

NULLABLE = {'null': True, 'blank': True}

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Наименование продукта')
    product_description = models.TextField(max_length=100, verbose_name='Описание продукта')
    product_image = models.ImageField(upload_to='product_images', verbose_name='Изображение продукта', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена продукта за единицу')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')  # Automatically set the date of
    date_last_modified = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения записи')  # Automatically set\

    def __str__(self):
        return f'{self.product_name} - {self.product_description}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Наименование категории')
    category_description = models.TextField(max_length=100, verbose_name='Описание категории')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')

    def __str__(self):
        return f'{self.category_name} - {self.category_description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'