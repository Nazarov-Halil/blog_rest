from django.urls import path
from apps.categories.views import CategoryViews

urlpatterns = [
    path('', CategoryViews.as_view(), name='list')
]