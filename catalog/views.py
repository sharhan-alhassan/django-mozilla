from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView

from django.shortcuts import get_list_or_404

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
    paginate_by = 2        # pagination for more than 4 records

    def get_query_set(self):
        return Book.objects.filter(title__icontains='count')[:5]

    """
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is some data'
        return context
    """

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book_detail.html'


class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'author_list'

class AuthorDetail(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'



