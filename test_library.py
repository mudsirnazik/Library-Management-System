from library import Library
from book import Book

def test_add_book():
    library = Library()
    book = Book("123", "Test", "Author", 2)
    library.add_book(book)
    assert "123" in library.books
