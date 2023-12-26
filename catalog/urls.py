from django.urls import path
from catalog.views import index, contact, home, ProductListView, CategoryListView, ProductDetailView

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('index/', index, name='index'),
    path('contacts/', contact, name='contact'),
    path('', home, name='home'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
]