from django import forms

from .models import Book, Entry


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 35,
                                                 'rows': 5})}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'page']
        labels = {'text': '',
                  'page': 'Page'}
        # Customizing the input widget for the field
        widgets = {'text': forms.Textarea(attrs={'cols': 40})}
