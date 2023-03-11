from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Blog


def index(request):
    context = {
        'blogs': Blog.objects.all()
    }
    return render(request, 'blog/index.html', context)


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'
    ordering = ['-date']


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Blog
    success_url = '/'

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', context={'title': 'About'})
