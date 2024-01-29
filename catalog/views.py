from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.models import Product, Category, Version
from catalog.forms import ProductForm, VersionForm, CategoryForm
from catalog.services import get_categories_cache


# Create your views here.
@login_required
def index(request):
    return render(request, 'catalog/index.html')


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category

    def fet_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category_list'] = get_categories_cache()
        return context_data


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_versions = Version.objects.filter(is_active=True)
        if active_versions:
            context['active_versions'] = active_versions
        else:
            context['active_versions'] = None
        return context



class ProductCategoryListView(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        return Product.objects.filter(category_id=category_pk)


class ProductDetailView(LoginRequiredMixin, DetailView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        context = {
            'object_list': Product.objects.filter(id=pk),
        }
        return render(request, 'catalog/product.html', context)


class ContactView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
    success_url = reverse_lazy("catalog:product_list")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        context = self.get_context_data()
        formset = context['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    success_url = reverse_lazy("catalog:product_list")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data


    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

    def test_func(self):
        return self.request.user.is_superuser


class CreateVersionView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.add_version'
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


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    permission_required = 'catalog.add_category'
    success_url = reverse_lazy("catalog:category_list")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

@login_required
def home(request):
    return render(request, 'catalog/home.html')
