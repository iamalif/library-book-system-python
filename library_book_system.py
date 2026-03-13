"""
Library Book System
Write a class called Book with private attributes:

isbn
title
author
is_borrowed (True/False)

Create a program where the user can:

Add books
List all available books
Borrow a book (sets is_borrowed to True)
Return a book
Search by author
"""

class Book:
    """Represents a library book with private attributes and getter/setter access.

    Uses name mangling (double underscore prefix) to enforce encapsulation,
    so attributes can only be accessed through the defined getter/setter methods.
    """

    def __init__(self, isbn, title, author, is_borrowed):
        # Private attributes — accessed via getters/setters to enforce encapsulation
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__is_borrowed = is_borrowed  # Boolean: True if the book is currently checked out

    def __str__(self):
        # Human-readable summary of the book, used when printing the object
        return f"isbn: {self.__isbn}, title: {self.__title}, author: {self.__author}, is_borrowed? {self.__is_borrowed}"

    # --- Setters: allow controlled modification of private attributes ---

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_is_borrowed(self, is_borrowed):
        # Used by borrow_book() and return_book() to toggle the borrow status
        self.__is_borrowed = is_borrowed

    # --- Getters: allow read access to private attributes ---

    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_is_borrowed(self):
        return self.__is_borrowed

# --- Input validation helpers ---
# These functions loop until the user provides valid input,
# preventing crashes from bad data types or empty strings.

def get_positive_int(prompt):
    """Repeatedly prompts the user until a non-negative integer is entered."""
    while True:
        try:
            num = int(input(prompt))
            if num < 0:
                print("Number needs to be positive.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def get_non_empty_string(prompt):
    """Repeatedly prompts the user until a non-empty string is entered."""
    while True:
        text = input(prompt)
        if text == "":
            print("Invalid input. Text field can not be empty.")
        else:
            return text

def user_menu():
    """Main interactive loop that displays the menu and routes user choices."""
    while True:
        print("\nEnter 1 to add a book")
        print("Enter 2 to borrow a book")
        print("Enter 3 to return a book")
        print("Enter 4 to list all available books")
        print("Enter 5 to search books by author")
        print("Enter 0 to Exit\n")

        choice = get_positive_int("Type your choice and press enter: ")

        if choice == 1:
            add_books()
        elif choice == 2:
            borrow_book()
        elif choice == 3:
            return_book()
        elif choice == 4:
            list_books()
        elif choice == 5:
            search_by_author()
        elif choice == 0:
            print("\nGoodbye!")
            break
        else:
            print("\nChoice needs to be between 0 to 5.")


# Global list that holds all Book objects added during the session
books = []

def add_books():
    """Prompts the user for book details and adds a new Book to the library.

    New books always start as not borrowed (is_borrowed=False).
    """
    isbn = get_positive_int("Enter ISBN number: ")
    title = get_non_empty_string("Enter book title: ")
    author = get_non_empty_string("Enter author name: ")
    is_borrowed = False  # All newly added books are available by default

    book = Book(isbn, title, author, is_borrowed)
    books.append(book)
    print(f"{book.get_title()} has been added.")

def list_books():
    """Prints all books in the library, or a message if the library is empty."""
    if len(books) == 0:
        print("No books available.")
    else:
        for book in books:
            print(book)

def borrow_book():
    """Marks a book as borrowed if it exists and is currently available.

    Uses book_found to distinguish between 'book not in library' and
    'book already borrowed', so the correct message is shown to the user.
    """
    isbn = get_positive_int("Enter ISBN number of the book to borrow: ")
    book_found = False  # Tracks whether a matching book was found in the list

    for book in books:
        if book.get_isbn() == isbn:
            book_found = True
            if book.get_is_borrowed() == False:
                # Book is available — mark it as borrowed
                book.set_is_borrowed(True)
                print(f"{book.get_title()} has been borrowed.")
                book_found = True
                break
            else:
                # Book exists but is already checked out
                print("Book is already borrowed.")
            break

    if not book_found:
        print("Book not found.")


def return_book():
    """Marks a book as returned if it exists and is currently borrowed.

    Uses book_found to distinguish between 'book not in library' and
    'book was never borrowed', so the correct message is shown to the user.
    """
    isbn = get_positive_int("Enter ISBN number of the book to return: ")
    book_found = False  # Tracks whether a matching book was found in the list

    for book in books:
        if book.get_isbn() == isbn:
            book_found = True
            if book.get_is_borrowed() == True:
                # Book is currently borrowed — mark it as returned
                book.set_is_borrowed(False)
                print(f"{book.get_title()} has been returned.")
                book_found = True
                break
            else:
                # Book exists but was not checked out
                print("This book was not borrowed.")
            break

    if not book_found:
        print("Book not found.")

def search_by_author():
    """Searches for available (not borrowed) books by a given author name.

    Only returns books that are currently not borrowed, since borrowed books
    are not available for other users to take.
    """
    author = get_non_empty_string("Enter author name: ")
    search_results = []
    for book in books:
        # Match on author name and only include books that are currently available
        if book.get_author() == author and book.get_is_borrowed() == False:
            search_results.append(book)
    if len(search_results) != 0:
        for book in search_results:
            print(book)
    else:
        print("No books available for that author")


def main():
    # Pre-populate the library with test data so the program is
    # immediately usable without needing to add books manually.
    # Note: test_book_2 and test_book_3 share the same author to
    # demonstrate the search_by_author functionality.
    test_book_1 = Book(111, "Title 1", "Author 1", False)
    test_book_2 = Book(222, "Title 2", "Author 2", False)
    test_book_3 = Book(333, "Title 3", "Author 2", False)
    books.append(test_book_1)
    books.append(test_book_2)
    books.append(test_book_3)

    user_menu()

# Only run the program when this file is executed directly,
# not when it is imported as a module
if __name__ == "__main__":
    main()