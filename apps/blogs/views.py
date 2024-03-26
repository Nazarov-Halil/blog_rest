from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView

from apps.blogs.forms import BlogForm, BlogImageForm
from apps.blogs.models import Blog, BlogImage


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'base.html'
    context_object_name = 'blog_blog'

    def get_queryset(self):
        return Blog.objects.all()


class CreateBlog(generic.CreateView):
    form_class = BlogForm
    template_name = 'create.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
