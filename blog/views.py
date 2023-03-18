from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DeleteView
from .models import Blog
from .forms import BlogResponseForm


def index(request):
    context = {
        'blogs': Blog.objects.all()
    }
    return render(request, 'blog/index.html', context)


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.order_by('-date').filter(parent=None)

class UserBlogListView(ListView):
    model = Blog
    template_name = 'blog/user_blog.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Blog.objects.order_by('-date').filter(author=user)

def blog_view(request, pk):
    if request.method == 'POST':
        form = BlogResponseForm(request.POST)
        form.instance.author = request.user
        form.instance.parent = get_object_or_404(Blog, id=pk)
        if form.is_valid():
            form.save()
    else:
        form = BlogResponseForm()
    
    context = {
        'object': Blog.objects.get(id=pk),
        'form': form,
        'responses': Blog.objects.order_by('date').filter(parent=pk)
    }
    return render(request, "blog/blog_detail.html", context)

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
