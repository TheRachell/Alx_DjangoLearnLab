from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITest(APITestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()

        # Authenticate user
        self.client.force_authenticate(user=self.user)

        # Create test data
        self.author = Author.objects.create(name="J.R.R. Tolkien")
        self.book = Book.objects.create(
            title="The Hobbit",
            publication_year=1937,
            author=self.author
        )
        self.list_url = reverse('book-list')  # /api/books/
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.id})  # /api/books/<id>/

    def test_create_book(self):
        data = {
            "title": "The Fellowship of the Ring",
            "publication_year": 1954,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "The Fellowship of the Ring")

    def test_get_book_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_single_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "The Hobbit")

    def test_update_book(self):
        data = {"title": "The Hobbit - Updated", "publication_year": 1937, "author": self.author.id}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "The Hobbit - Updated")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books_by_title(self):
        response = self.client.get(f'{self.list_url}?title=The Hobbit')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "The Hobbit")

    def test_search_books(self):
        response = self.client.get(f'{self.list_url}?search=tolkien')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "The Hobbit")

    def test_order_books_by_year_desc(self):
        Book.objects.create(title="New Book", publication_year=2000, author=self.author)
        response = self.client.get(f'{self.list_url}?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2000)

    def test_permission_for_unauthenticated_user(self):
        self.client.logout()
        response = self.client.post(self.list_url, {
            "title": "Unauthorized Book",
            "publication_year": 2024,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

