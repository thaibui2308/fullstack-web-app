from django.shortcuts import render, redirect
from .models import Book, Entry
from .forms import BookForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.
def index(request):
    """Web application homepage"""
    return render(request, 'book_logs/index.html')


@login_required
def books(request):
    """Show all book currently reading"""
    # When a user logs in, the request object will have an attribute of
    # request.user that stores information about the user
    books = Book.objects.filter(owner=request.user).order_by('date_added')
    context = {'books': books}
    return render(request, 'book_logs/books.html', context)


@login_required
def book(request, book_id):
    """Show the book and all its entries"""
    book = Book.objects.get(id=book_id)
    # Check whether the user's req URL matches with the owner of that data
    if book.owner != request.user:
        raise Http404
    entries = book.entry_set.order_by('-date_added')
    context = {
        'book': book,
        'entries': entries
    }
    return render(request, 'book_logs/book.html', context=context)


@login_required
def new_book(request):
    """Add a new book"""
    if request.method != "POST":
        # No data submitted create a blank form
        form = BookForm()
    else:
        # POST data submitted, processing it.
        form = BookForm(data=request.POST)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.owner = request.user
            new_book.save()
            # Redirecting the user back to the books page
            return redirect('book_logs:books')

    context = {'form': form}
    return render(request, 'book_logs/new_book.html', context)


@login_required
def new_entry(request, book_id):
    """Add a new entry for a specific book"""
    book = Book.objects.get(id=book_id)

    if book.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data
        form = EntryForm()
    else:
        # Data submitted
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # Create a new entry object and assigns it to new_entry without saving it to the database
            new_entry = form.save(commit=False)
            new_entry.book = book
            new_entry.save()
            # Two arguments:
            # First: the view function we want to redirect to
            # Second: the additional arg for that view function
            return redirect('book_logs:book', book_id=book_id)

    context = {
        'book': book,
        'form': form
    }
    return render(request, 'book_logs/new_entry.html', context=context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    book = entry.book

    if book.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request, refill form with the current entry
        form = EntryForm(instance=entry)
    else:
        # Processing newly-posted data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_logs:book', book_id=book.id)

    context = {
        'entry': entry,
        'book': book,
        'form': form
    }
    return render(request, 'book_logs/edit_entry.html', context=context)

@login_required
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('book_logs:books')

@login_required
def delete_entry(request,book_id, entry_id):
    entry = Entry.objects.get(id=entry_id)
    entry.delete()
    return redirect('book_logs:book', book_id=book_id)
