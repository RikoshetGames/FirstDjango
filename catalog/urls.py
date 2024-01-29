from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (index, home, CategoryListView, ProductDetailView, ProductCategoryListView, ContactView, \
                           ProductCreateView, ProductUpdateView, ProductDeleteView, ProductListView, CreateVersionView, \
                           CategoryCreateView,)

from catalog.apps import CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('index/', index, name='index'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('', home, name='home'),
    path('product_list/<int:pk>/', ProductCategoryListView.as_view(), name='product_list'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('versions/create/', CreateVersionView.as_view(), name='create_version'),
    path('category_list/create/', CategoryCreateView.as_view(), name='create_category'),
]