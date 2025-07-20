# Import the Book model
from bookshelf.models import Book

# retrieve all attributes
books = Book.objects.get(title='1984')