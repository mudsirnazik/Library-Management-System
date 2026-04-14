def search_by_title(library, title):
    return [book for book in library.books.values() if title.lower() in book.title.lower()]

def search_by_author(library, author):
    return [book for book in library.books.values() if author.lower() in book.author.lower()]

def search_by_isbn(library, isbn):
    return library.books.get(isbn, None)
