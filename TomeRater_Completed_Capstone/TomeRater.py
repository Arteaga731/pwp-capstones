#Capstone: create an application called TomeRater that allows users to read and rate books.

class User:
    '''Creates User objects to keep track of users'''

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {} 

    def get_email(self):
        return self.email 

    def change_email(self, address):
        self.email = address
        print("This user's email has been updated.")
    
    def read_book(self, book, rating=None):
        return self.books.update({book:rating})
            
    def get_average_rating(self):
        sum_total = 0
        for rating in self.books.values():
            if rating:
                sum_total += rating  
        return sum_total/(len(self.books))

    def __repr__(self):
        return "{name}, email: {email}, books read: 7".format(name=self.name, email=self.email) 

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name and self.email == other.email 
        return False

    def __ne__(self, other):
        return self.name != other.name or self.email != other.email
    
    
class Book:
    '''Creates Book objects to keep track of books and define what is a book.'''
    
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
   
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("This book's isbn has been updated")
    
    def add_rating(self, rating):
        if rating >= 0 and rating <= 4: 
            self.ratings.append(rating)
        else: 
            print("Invalid Rating")
                        
    def get_average_rating(self):
        sum_total = 0
        for rating in self.ratings:
            sum_total += rating
        return sum_total/(len(self.ratings))
    
    def __hash__(self):
        return hash((self.title, self.isbn))
            
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.title == other.title and self.isbn == other.isbn
        return False
    
    def __ne__(self, other):
        return self.title != other.title or self.isbn != other.isbn
    
    def __repr__(self):
        return ("{}".format(self.title))
    
    
class Fiction(Book):
    '''Subclass of Book object meant to define fiction, one of two types of books.'''
    
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
   
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{title}, by {author}".format(title=self.title, author=self.author)
        
        
class Non_Fiction(Book):
    '''Subclass of Book object meant to define non-fiction, which along side the
    pre-defined Fiction subclass, make-up the two types of books.'''
    
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level 
    
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)
          
            
class TomeRater:
    '''This is the main class that allows interaction with the other four pre-defined classes to
      create and allow users to read and rate book.'''
             
    def __init__(self):
        self.users = {} 
        self.books = {} 
        self.user_books_read = {}
       
    def create_book(self, title, isbn):
        return Book(title, isbn) 
 
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)
    
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)
    
    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email)
        self.user_books_read.update({email:1})
        if user:
            user.read_book(book, rating)
            if rating:
                book.add_rating(rating)
            if book not in self.books:
                self.books.update({book:1}) 
            self.books[book] += 1
            self.user_books_read[email] += 1
        else:
            return "No user with email{email}!".format(email=email)
                
    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books is not None:
            for book in user_books:
                return self.add_book_to_user(book, email)
 
    def print_catalog(self):
        for key in self.books.keys():
            print(key)
    
    def print_users(self):
        for key in self.users.keys():
            print(key)
  
    def get_most_read_book(self):
        book_read = None
        times_read = float()
        for book, read in self.books.items():
            if read > times_read:
                book_read = book
                times_read = read
        return book_read
                 
    def highest_rated_book(self):   
        book_name = None
        highest_rating = float()
        for key, value in self.books.items():
            if key.get_average_rating() > highest_rating:
                highest_rating = value
                book_name = key
        return book_name
       
    def most_positive_user(self):
        return sorted(self.users.items(), key=lambda x: x[1].get_average_rating(), reverse=True)[0][0]                

# Get creative part of assignment: More sophisticated analysis methods.
    def get_n_most_read_books(self, n):
        n_most_read = sorted(self.books, key=self.books.__getitem__, reverse=True)
        return n_most_read[:n]
        
    def get_n_most_prolific_readers(self, n):
        most_prolific = sorted(self.user_books_read, key=self.user_books_read.__getitem__, reverse=True)
        return most_prolific[:n]
        


