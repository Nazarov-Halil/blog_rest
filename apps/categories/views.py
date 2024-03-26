from django.shortcuts import render
from django.views.generic import ListView

from apps.categories.models import Categories


class CategoryViews(ListView):
    model = Categories
    template_name = 'base.html'
    context_object_name = 'category'

    def get_queryset(self):
        return Categories.objects.all()
