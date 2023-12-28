# Create your models here.

from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    blog_title = models.CharField(max_length=100, verbose_name='Название блога')
    blog_description = models.TextField(max_length=200, verbose_name='Описание блога')
    blog_image = models.ImageField(upload_to='blog_images', verbose_name='Изображение блога', **NULLABLE)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания блога')

    is_published = models.BooleanField(default=True, verbose_name='Опубликован')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)

    def __str__(self):
        return f'{self.blog_title} - {self.blog_description}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'