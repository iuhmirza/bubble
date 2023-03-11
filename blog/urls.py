from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView
from . import views

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-index'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/new/', BlogCreateView.as_view(), name='blog-create'),
    path('about/', views.about, name='blog-about')
]

