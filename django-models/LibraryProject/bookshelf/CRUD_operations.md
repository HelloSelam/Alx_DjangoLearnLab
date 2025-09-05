# CRUD Operations with the Book Model

This document demonstrates basic **Create, Retrieve, Update, and Delete (CRUD)** operations on the `Book` model using Django’s ORM in the Django shell.

---

## 1. Create a Book

```python
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book

# Output: <Book: 1984 by George Orwell (1949)>


2. Retrieve the Book
# Retrieve the book we just created
book = Book.objects.get(id=1)
book.title, book.author, book.publication_year

# Output: ('1984', 'George Orwell', 1949)


3. Update the Book
# Update the title of the book
book.title = "Nineteen Eighty-Four"
book.save()
book.title

# Output: 'Nineteen Eighty-Four'


4. Delete the Book
# Delete the book
book.delete()

# Verify deletion
Book.objects.all()

# Output: (<number of rows deleted>, {'bookshelf.Book': 1})
<QuerySet []>

