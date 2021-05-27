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
    # Page to delete a book out of a collection
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    # Page to create new book topic
    path('new_book/', views.new_book, name='new_book'),
    # Page to add new entry to a book
    path('new_entry/<int:book_id>/', views.new_entry, name="new_entry"),
    # Page to edit entry of a book
    path('edit_entry/<int:entry_id>/', views.edit_entry, name="edit_entry"),
    # Page to delete an entry out of a book
    path('delete_entry/<int:book_id>/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]
