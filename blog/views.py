from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
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
    

def about(request):
    return render(request, 'blog/about.html', context={'title': 'About'})
