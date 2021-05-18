


from django.urls import path 

from .views import index, BookListView, BookDetailView, AuthorList, AuthorDetail, LoanedBooksByUserListView, renew_book_by_librarian

urlpatterns = [
    path('', index, name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-borrowed-books'),
    path('book/<uuid:pk>/renew/', renew_book_by_librarian, name='renew-book-librarian'),
]