# Create your views here.

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from pytils.translit import slugify

from blog.models import Blog

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        phone = request.POST.get('phone', )
        message = request.POST.get('message', )
        return render(request, 'blog/contacts.html', context={'name': name, 'phone': phone, 'message': message})
    return render(request, 'blog/contacts.html')


class BlogCreateView(CreateView):
    model = Blog
    fields = ('blog_title', 'blog_description', 'blog_image', 'is_published',)
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):    # Задание 3: выводить в список статей только те, которые имеют положительный признак публикации
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.blog_title)    # В консоли нужно установить модуль pytils
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_description', 'blog_image', 'is_published',)
    success_url = reverse_lazy('view')


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'

    def get_queryset(self, args, **kwargs):    # Задание 3: выводить в список статей только c положительным признаком публикации
        queryset = super().get_queryset(args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

class BlogDetailView(DetailView):
    # model = Blog

    def get(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        context = {
            'object_list': Blog.objects.filter(id=pk),
        }
        return render(request, 'blog/blog_detail.html', context)

    def get_object(self, queryset=None):    # Задание 3: при открытии отдельной статьи увеличивать счетчик просмотров;
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
