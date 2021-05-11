
from django.urls import path 
from . import views

from .views import index, BookListView

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BooListView.as_view(), name='books'),
]