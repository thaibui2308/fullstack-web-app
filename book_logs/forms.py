from django import forms

from .models import Book, Entry


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # Customizing the input widget for the field
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
