# Creating a Book instance
Command:
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

Expected Output:
<Book: 1984 by George Orwell (1949)>
