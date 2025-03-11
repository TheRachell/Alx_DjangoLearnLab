Create Operation 

command: 
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

Output:
<Book: 1984 by George Orwell (1949)>


Retrieve Operation 

Command:
Book.objects.all()

Output:
<QuerySet [<Book: 1984 by George Orwell (1949)>]>


Update Operation 

Command:
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

Output:
<Book: Nineteen Eighty-Four by George Orwell (1949)>


Delete Operation

Command:
book.delete()

Output:
(1, {'bookshelf.Book': 1})

