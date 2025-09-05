
---

### 📄 `update.md`
```markdown
# Update Operation

This demonstrates how to update an existing `Book` instance.

```python
from bookshelf.models import Book

# Retrieve the book and update the title
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# Output: 'Nineteen Eighty-Four'