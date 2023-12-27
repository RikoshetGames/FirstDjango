from django.contrib import admin

from blog.models import Blog

@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog_title', 'blog_description', 'blog_image', 'is_published',)
    list_filter = ('is_published',)
    search_fields = ('blog_title', 'blog_description',)