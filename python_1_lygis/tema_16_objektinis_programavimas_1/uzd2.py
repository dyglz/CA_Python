# Maža biblioteka

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_title(self) -> str:
        return f"Title: {self.title}"

    def get_author(self) -> str:
        return f"Author: {self.author}"
    

book_1 = Book(title="Pride and Prejudice", author="Jane Austen")
book_2 = Book(title="Hamlet", author="William Shakespeare")
book_3 = Book(title="War and Peace", author="Leo Tolstoy")
book_4 = Book(title="Harry Potter", author="J.K. Rowling")


print(book_1.title)  # Harry Potter
print(book_1.author)  # J.K. Rowling
print(book_1.get_title())  # Title: Harry Potter
print(book_1.get_author())  # Author: J.K. Rowling