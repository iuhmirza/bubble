from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogDeleteView, UserBlogListView
from . import views

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-index'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/new/', BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog-delete'),
    path('user/<str:username>', UserBlogListView.as_view(), name='user-blogs'),
    path ('about/', views.about, name='blog-about')
]

