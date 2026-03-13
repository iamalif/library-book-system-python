# library-book-system-python

A Python command-line application to manage a library book system, 
built using Object-Oriented Programming (OOP) principles.

## About
This program simulates a basic library system where users can add 
books, borrow and return them, list all available books, and search 
by author via a console menu. Built as a personal OOP practice project.

## Features
- Book class with private attributes (ISBN, title, author, borrow status)
- Getter and setter methods for all attributes
- Add new books to the library
- Borrow a book with availability check
- Return a borrowed book
- List all books in the system
- Search available books by author
- Pre-loaded test books for quick testing
- Input validation throughout

## How to Run
```bash
python library_book_system.py
```

## Built With
- Python 3
- OOP — classes, private attributes, getter/setter methods
- Input validation functions for clean, reusable code

## Test Books
Three test books are pre-loaded on launch for quick testing:
| ISBN | Title | Author | Available |
|------|-------|--------|-----------|
| 111 | Title 1 | Author 1 | Yes |
| 222 | Title 2 | Author 2 | Yes |
| 333 | Title 3 | Author 2 | Yes |
