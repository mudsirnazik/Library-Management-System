def issue_book(library, isbn, member):
    if isbn in library.books and library.books[isbn].copies > 0:
        library.books[isbn].copies -= 1
        member.borrowed_books.append(isbn)
        return True
    return False

def return_book(library, isbn, member):
    if isbn in member.borrowed_books:
        library.books[isbn].copies += 1
        member.borrowed_books.remove(isbn)
        return True
    return False
