from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        # Create an author
        self.author = Author.objects.create(name="J.K. Rowling")
        
        # Create a book
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author
        )

    # Test listing books
    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # Test creating a book (authenticated)
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-create')
        data = {
            "title": "Harry Potter and the Chamber of Secrets",
            "publication_year": 1998,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    # Test creating a book (unauthenticated)
    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Test updating a book
    def test_update_book(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-update', args=[self.book.id])
        data = {
            "title": "Harry Potter Updated",
            "publication_year": 1997,
            "author": self.author.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter Updated")

    # Test deleting a book
    def test_delete_book(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
