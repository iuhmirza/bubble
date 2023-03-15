from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
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

class UserBlogListView(ListView):
    model = Blog
    template_name = 'blog/user_blog.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Blog.objects.order_by('-date').filter(author=user)


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/'

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', context={'title': 'About'})
