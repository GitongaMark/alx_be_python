class Book:
   
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False  

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
        
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
        
    def is_available(self):
        return not self._is_checked_out


class Library:

    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    def check_out_book(self, title: str):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title: str):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return
                else:
                    print(f"'{title}' is already in the library.")
                    return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
       available_books = [book for book in self._books if book.is_available()]
       for book in available_books:
         print(f"{book.title} by {book.author}")