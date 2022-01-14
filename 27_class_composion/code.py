class BookShelf():
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"

class Book():
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Book: {self.name}"

book1 = Book("harry potter")
book2 = Book("lord of the rings")

bookshelf = BookShelf(book1, book2)

print(bookshelf)
print(book1)
print(book2)       

print(bookshelf.books[0].name)