
from django.urls import path 

from .views import index, BookListView, BookDetailView

urlpatterns = [
    path('', index, name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book-detail'),
]