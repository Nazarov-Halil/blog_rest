from rest_framework import viewsets, generics

from apps.blogs.api.serializers import BlogSerializer, BlogImageSerializer, BlogCreateSerializer
from apps.blogs.models import Blog, BlogImage


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return BlogCreateSerializer
        elif self.action == 'retrieve':
            return BlogSerializer
        return self.serializer_class


class BlogImageCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer


class BlogUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogImageUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer
