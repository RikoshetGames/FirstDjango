from django.urls import path
from catalog.views import index, home, ProductListView, CategoryListView, ProductDetailView, ProductCategoryListView, ContactView

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('index/', index, name='index'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('', home, name='home'),
    path('product_list/<int:pk>/', ProductCategoryListView.as_view(), name='product_list'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
]