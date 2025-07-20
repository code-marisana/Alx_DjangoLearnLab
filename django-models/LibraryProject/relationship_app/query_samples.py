from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.get(name="Author Name")
books_by_author = author.books.all()

library = Library.objects.get(name="Library Name")
books_in_library = library.books.all()

library = Library.objects.get(name="Library Name")
librarian_lib = Librarian.objects.get(library=library)

