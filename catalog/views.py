from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from catalog.models import Book, Author, BookInstance, Genre, Language

# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The all() is simplified by default
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)

class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    # queryset = Book.objects.filter(title__icontains='count')[:5]
    template_name = 'book_list.html'

    def get_query_set(self):
        return Book.objects.filter(title__icontains='count')[:5]

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail'