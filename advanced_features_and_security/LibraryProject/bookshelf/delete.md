
---

### 📄 `delete.md`
```markdown
# Delete Operation

This demonstrates how to delete a `Book` instance.

```python
from bookshelf.models import Book

# Retrieve and delete the book
book = Book.objects.get(id=1)
book.delete()

# Verify deletion
Book.objects.all()
# Output: (<number of rows deleted>, {'bookshelf.Book': 1})
# QuerySet []