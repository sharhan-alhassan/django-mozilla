
from django import forms
from django.db import models
from django.views.generic import TemplateView, ListView, DetailView

from django.shortcuts import get_list_or_404

from catalog.models import Book, Author, BookInstance, Genre, Language

from django.contrib.auth.mixins import LoginRequiredMixin

import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required, permission_required

from .forms import RenewBookForm

# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The all() is simplified by default
    num_authors = Author.objects.count()

    # session to get visit counts
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visists'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
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


class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = BookInstance
    template_name = 'bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

@login_required
def renew_book_by_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the FORM data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request(binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in the form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to new URL:
            return HttpResponseRedirect(reverse('/'))

    # If this is a GET (or any other method) create the Default form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
        
    context = {
        'form': form,
        'book_instance': book_instance
    }

    return render(request, 'book_renew_by_librarian', context)

