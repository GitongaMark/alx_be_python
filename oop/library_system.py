# library_system.py

class Book:
    def __init__(self, title, author):
        """Initialize a Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return string representation of a Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook, including file size in KB."""
        super().__init__(title, author)  # Call base class initializer
        self.file_size = file_size

    def __str__(self):
        """Return string representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook, including page count."""
        super().__init__(title, author)  # Call base class initializer
        self.page_count = page_count

    def __str__(self):
        """Return string representation of a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize an empty library."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only Book or subclasses can be added to the library.")

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)
