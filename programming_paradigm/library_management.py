class Book:
    """Represents a book with a title, author, and checked-out status."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # The task asks for a private attribute, so we use a single underscore
        self._is_checked_out = False # Changed name for clarity and convention

class Library:
    """Manages a collection of Book objects."""
    def __init__(self):
        # Private list to store book objects
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds a book by title and marks it as checked out."""
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                print(f"You have checked out '{title}'.")
                return
        print(f"Sorry, '{title}' is either already checked out or not in the library.")

    def return_book(self, title):
        """Finds a book by title and marks it as returned (not checked out)."""
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                print(f"You have returned '{title}'.")
                return
        print(f"Sorry, '{title}' cannot be returned or is not in the library.")

    def list_available_books(self):
        """Prints a list of all books that are not checked out."""
        available_books = []
        for book in self._books:
            if not book._is_checked_out:
                available_books.append(book)
        
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")