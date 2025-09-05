from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Library
from .models import Book

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view: show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"