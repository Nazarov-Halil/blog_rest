from django.urls import path
from apps.blogs.views import BlogListView, CreateBlog

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('create', CreateBlog.as_view(), name='create')
]