from relationship_app.models import Author, Book, Library, Librarian
author_name = ''
library_name = ''
author = Author.objects.get(name=author_name)
books_by_author = author.books.all()

library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

library = Library.objects.get(name=library_name)
librarian_lib = Librarian.objects.get(library=library)

