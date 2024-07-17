# Define a class Library that contains a list of books. 
# Implement a constructor that initializes the library with a name and an empty list of books. 
# Add methods to add a book, 
# remove a book by name, and find a book by author. 
# Write a method to display all books in the library.

class Library:

    def __init__(self, library_name,books,author):
      self.library_name = library_name
      self.books = books
      self.author = author
    
    def addBook(self,book,author):
        list = [book,author]
        self.books.append(list)
        
    def displayAllBooks(self):
        print(self.books)
    
    def findBookByAuthor(self,author):
        
        newList = []
        
        for book in self.books:
            if author==book[1]:
                newList.append(book)
        
        if len(newList)==0:
            print("No book found")
        else:
            print(newList)
    
    def removeBookByAuthor(self,author):  # thoreau

        newlist = []
        
        for book in self.books:
            if author!=book[1]:
               newlist.append(book)
        
        if self.books==newlist:
            print("No author found")
        else:
            self.books = newlist               
    
    def removeAllBooks(self):
        self.books.clear()
      
    
l1 = Library("College Library",[],"")
l1.addBook("walden","thoreau")
l1.addBook("civil disobediance","thoreau")
l1.addBook("lighthouse","dhumketu")

l1.displayAllBooks()

l1.removeBookByAuthor("dhumketu")
l1.removeBookByAuthor("dhumketu")
l1.findBookByAuthor("dhumketu")

l1.displayAllBooks()