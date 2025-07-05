class Book:
    def __init__(self, title, author):
        self.title = title                  # Public attribute: book title
        self.author = author                # Public attribute: book author
        self._is_checked_out = False        # Private attribute: whether the book is checked out

    def check_out(self):
        """Mark the book as checked out"""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (not checked out)"""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is currently available"""
        return not self._is_checked_out

    def __str__(self):
        """Return a readable string representation of the book"""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a book to the library"""
        self._books.append(book)

    def check_out_book(self, title):
        """Find a book by title and check it out if available"""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        """Return a book by title if it is currently checked out"""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"'{title}' was not checked out.")

    def list_available_books(self):
        """Print all books that are currently available"""
        for book in self._books:
            if book.is_available():
                print(book)
