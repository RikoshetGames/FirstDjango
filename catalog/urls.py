from django.urls import path
from catalog.views import index, contact, home

urlpatterns = [
    # path('', index),
    # path('', contact),
    path('', home)
]