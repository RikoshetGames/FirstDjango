from django.urls import path
from catalog.views import index, contact, home, product

urlpatterns = [
    path('index/', index, name='index'),
    path('contacts/', contact, name='contact'),
    path('', home, name='home'),
    path('product/<int:pk>', product, name='product'),
]