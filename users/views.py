from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm, UserCreationForm


# Create your views here.
def register(request):
    """Register a new account/user"""
    # Always displaying a blank form for the GET request
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_logs:index')
    else:
        form = NewUserForm()

    # Display a blank or invalid form
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context=context)

