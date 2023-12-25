from django.shortcuts import render
from catalog.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'object_list': products
    }
    return render(request, 'catalog/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name is not None and email is not None:
            return render(request, 'catalog/contacts.html', context={'name': name, 'email': email})
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')


# def product(request, pk):
#     products = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(category_id=pk),
#         'title': products.product_name
#     }
#     return render(request, 'catalog/product.html', context)

def product(request, pk):
    products = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(id=pk),
    }
    return render(request, 'catalog/product.html', context)