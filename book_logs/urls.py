"""URL patterns for book logs"""

from django.urls import path
from . import views

app_name = "book_logs"
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all in-progress books
    path('books/', views.books, name='books'),
    # Detail page for a single book.
    path('books/<int:book_id>/', views.book, name='book'),
    # Page to create new book topic
    path('new_book/', views.new_book, name='new_book'),
    # Page to add new entry to a book
    path('new_entry/<int:book_id>/', views.new_entry, name="new_entry"),
    # Page to edit entry of a book
    path('edit_entry/<int:entry_id>/', views.edit_entry, name="edit_entry")
]
