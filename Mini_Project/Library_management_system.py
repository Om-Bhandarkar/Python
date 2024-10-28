class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            is_checked_out = True
            print(f"{self.title} has been checked out.")
        else:   
            print(f"{self.title} has already checked out.")


    def return_book(self):
        if self.is_checked_out :
            self.is_checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not checked out.")

    
    def __str__(self):
        status = "Checked out " if self.is_checked_out else "Available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status:{status}"



class EBook(Book):
    def __init__(self,title,author,isbn,filesize):
        super().__init__(title,author,isbn)
        self.filesize = filesize
    def __str__(self):
        return super().__str__() + f", File Size: {self.filesize} MB" 
    

class PrintedBook(Book):
    def __init__(self,title,author,isbn,page_count):
        super().__init__(title,author,isbn)
        self.page_count = page_count

    def __str__(self):
        return super().__str__() + f", Page Count: {self.page_count}" 
    
class Library:
    def __init__(self) :
        self.books= {}

    def add_book(self,book):
        self.books[book.isbn] = book
        print(f"Added : {book}")

    def remove_book(self,isbn):
        if isbn in self.books:
            del self.books[isbn]
            print(f"Removed book with ISBN: {isbn}")
        else:
            print(f"No book found with ISBN :{isbn}")

    def check_out_book(self,isbn):
        if isbn in self.books:
            self.books[isbn].check_out()
        else:
            f"No book found with ISBN : {isbn}"
        
    def return_book(self,isbn):
        if isbn in self.books:
            self.books[isbn].return_book()
        else:
            f"No book found with ISBN : {isbn}"

    def list_books(self):
        print("Library Books : ")
        for book in self.books.values():
            print(book)

if __name__ == '__main__':

    ebook = EBook("Python Programming", "John Doe", "1234567890", 2.5)
    
    printed_book = PrintedBook("Data Structures", "Jane Smith", "0987654321", 300)
    
    library = Library()
    library.add_book(ebook)
    library.add_book(printed_book)

    library.list_books()   
    library.remove_book("1234567890") 
    library.list_books()
