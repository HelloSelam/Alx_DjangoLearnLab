from django import forms
from .models import Book


class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_date"]

    # Extra validation (example: title must not be empty)
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if not title or title.strip() == "":
            raise forms.ValidationError("Title cannot be empty")
        return title
