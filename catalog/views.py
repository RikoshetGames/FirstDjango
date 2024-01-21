from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.models import Product, Category, Version
from catalog.forms import ProductForm, VersionForm


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')


class CategoryListView(ListView):
    model = Category


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_versions = Version.objects.filter(is_active=True)
        if active_versions:
            context['active_versions'] = active_versions
        else:
            context['active_versions'] = None
        return context



class ProductCategoryListView(ListView):
    model = Product

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        return Product.objects.filter(category_id=category_pk)


class ProductDetailView(DetailView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        context = {
            'object_list': Product.objects.filter(id=pk),
        }
        return render(request, 'catalog/product.html', context)


class ContactView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class CreateVersionView(View):
    def get(self, request):
        form = VersionForm()
        return render(request, 'catalog/create_version.html', {'form': form})

    def post(self, request):
        form = VersionForm(request.POST)
        if form.is_valid():
            version = form.save(commit=False)
            product_id = version.product_id


            Version.objects.filter(product_id=product_id).update(is_active=False)

            version.is_active = True
            version.save()

            return redirect('catalog:product_list')
        return render(request, 'catalog/create_version.html', {'form': form})


def home(request):
    return render(request, 'catalog/home.html')
