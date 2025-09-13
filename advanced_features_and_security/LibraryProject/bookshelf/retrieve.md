
---

### 📄 `retrieve.md`
```markdown
# Retrieve Operation

This demonstrates how to retrieve a `Book` instance from the database.

```python
from bookshelf.models import Book

# Retrieve the book with ID 1
book = Book.objects.get(id=1)
book.title, book.author, book.publication_year
# Output: ('1984', 'George Orwell', 1949)