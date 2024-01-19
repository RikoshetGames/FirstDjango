from django.urls import path
from catalog.views import index, home, ProductListView, CategoryListView, ProductDetailView, ProductCategoryListView, ContactView, ProductCreateView, ProductUpdateView, ProductDeleteView

from catalog.apps import CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('index/', index, name='index'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('', home, name='home'),
    path('product_list/<int:pk>/', ProductCategoryListView.as_view(), name='product_list'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]