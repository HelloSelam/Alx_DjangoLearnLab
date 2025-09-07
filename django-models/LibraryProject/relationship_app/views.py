from django.shortcuts import render, redirect 
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view: show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# --- Registration View ---
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            return redirect("list_books")  # Redirect somewhere meaningful
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})