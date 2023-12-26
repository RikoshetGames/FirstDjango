from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from catalog.models import Product, Category

# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')


class CategoryListView(ListView):
    model = Category


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        context = {
            'object_list': Product.objects.filter(id=pk),
        }
        return render(request, 'catalog/product.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name is not None and email is not None:
            return render(request, 'catalog/contacts.html', context={'name': name, 'email': email})
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')
