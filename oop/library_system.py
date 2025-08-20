#!/usr/bin/python3
"""
Module defining classes for a library system: Book, EBook, PrintBook, and Library.
Demonstrates inheritance and composition.
"""

class Book:
    """Base class for all books."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    # The string representation method is key for printing polymorphic objects
    def __str__(self):
        """Returns the basic string representation of the book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns the string representation including file size."""
        # Correctly call the parent's method and add extra info
        return f"E{super().__str__()}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """Derived class representing a physical print book."""
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Returns the string representation including page count."""
        # This fixes your original error by using the instance variable 'self.page_count'
        return f"Print{super().__str__()}, Page Count: {self.page_count}"


class Library:    
    """A class representing a library managing a collection of books."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book object (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Lists all books in the library using polymorphism."""
        if not self.books:
            print("The library is empty.")
            return

        for book in self.books:
            # The core fix: Python automatically calls the object's __str__ method.
            # Since EBook and PrintBook have their own __str__ methods,
            # the correct format (including file size or page count) is printed.
            print(str(book))