from book import Book
from member import Member
from library import Library
from issue_return import issue_book, return_book
from search import search_by_title

def main():
    library = Library()
    member = Member("1", "Ali")

    while True:
        print("\n1. Add Book\n2. Search Book\n3. Issue Book\n4. Return Book\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            isbn = input("ISBN: ")
            title = input("Title: ")
            author = input("Author: ")
            copies = int(input("Copies: "))
            library.add_book(Book(isbn, title, author, copies))

        elif choice == "2":
            title = input("Enter title: ")
            results = search_by_title(library, title)
            for book in results:
                print(book.title, book.author, book.copies)

        elif choice == "3":
            isbn = input("Enter ISBN: ")
            if issue_book(library, isbn, member):
                print("Book issued")
            else:
                print("Not available")

        elif choice == "4":
            isbn = input("Enter ISBN: ")
            if return_book(library, isbn, member):
                print("Book returned")
            else:
                print("Error")

        elif choice == "5":
            break

if __name__ == "__main__":
    main()
