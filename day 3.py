class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
        else:
            raise Exception(f"The book '{self.title}' is currently not available.")

    def return_book(self):
        self.is_available = True


class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            raise Exception(f"The book '{book.title}' is currently not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            raise Exception(f"The book '{book.title}' was not borrowed by {self.name}.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def lend_book(self, book_id, member_id):
        book = next((b for b in self.books if b.id == book_id), None)
        member = next((m for m in self.members if m.id == member_id), None)
        if book and member:
            member.borrow_book(book)
        else:
            raise Exception("Book or Member not found")

    def return_book(self, book_id, member_id):
        book = next((b for b in self.books if b.id == book_id), None)
        member = next((m for m in self.members if m.id == member_id), None)
        if book and member:
            member.return_book(book)
        else:
            raise Exception("Book or Member not found")


library = Library()

book1 = Book("B001", "1999", "Tata Cantik")
book2 = Book("B002", "Love her is sick", "Azzam")
library.add_book(book1)
library.add_book(book2)

member1 = Member("M001", "Luthfi")
member2 = Member("M002", "Anita")
library.register_member(member1)
library.register_member(member2)

library.lend_book("B001", "M001")
print(f"{member1.name} borrowed '{book1.title}'")

library.return_book("B001", "M001")
print(f"{member1.name} returned '{book1.title}'")

print(f"Is '{book1.title}' available? {'Yes' if book1.is_available else 'No'}")
