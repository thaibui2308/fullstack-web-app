from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    """A book the user is currently reading."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of a model"""
        return self.text


class Entry(models.Model):
    """Related to the book being read"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    page = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        if len(self.text) >= 30:
            return f"{self.text[:25]}..."
        else:
            return self.text
