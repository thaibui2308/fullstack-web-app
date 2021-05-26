from django.contrib import admin

from .models import Book, Entry

admin.site.register(Book)
admin.site.register(Entry)
