#!/usr/bin/python3
"""
This module defines the Book and Library classes for a simple library management system.
"""

class Book:
    """Represents a book with a title, author, and checked-out status."""

    def __init__(self, title, author):
        """Initializes a new Book instance."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        # This method now lives inside the Book class.
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned (not checked out)."""
        # This method also lives inside the Book class.
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False


class Library:
    """Manages a collection of Book objects."""

    def __init__(self):
        """Initializes a new Library instance with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds a book by title and tells it to check itself out."""
        for book in self._books:
            if book.title == title:
                # Call the book's OWN check_out method
                if book.check_out():
                    print(f"You have checked out '{title}'.")
                else:
                    print(f"Sorry, '{title}' is already checked out.")
                return
        print(f"Sorry, the book '{title}' was not found in the library.")

    def return_book(self, title):
        """Finds a book by title and tells it to return itself."""
        for book in self._books:
            if book.title == title:
                # Call the book's OWN return_book method
                if book.return_book():
                    print(f"You have returned '{title}'.")
                else:
                    print(f"Sorry, '{title}' was not checked out.")
                return
        print(f"Sorry, the book '{title}' was not found in the library.")

    def list_available_books(self):
        """Prints a list of all books that are not checked out."""
        available_books = [book for book in self._books if not book._is_checked_out]
        
        if not available_books:
            print("No books are currently available.")
        else:
            print("Available books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")