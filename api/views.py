from django.shortcuts import render
from rest_framework import generics, permissions, filters 
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend

# ListView - Retrieve all books
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]

    filterset_fields = ['author','title', 'publication_year']

    search_fields = ['title', 'author__name']

    ordering_fields = ['publication_year', 'title']

# DetailView - Retrieve a single book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# CreateView - Add a new book (Restricted to authenticated users)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# UpdateView - Modify an existing book (Restricted to authenticated users)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# DeleteView - Remove a book (Restricted to authenticated users)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

