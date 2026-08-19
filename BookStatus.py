from abc import ABC,abstractmethod
class Book(ABC):
    def __init__(self,t,a,y):
        self._title=t
        self._author=a
        self._yearPublished=y

    @abstractmethod
    def displayStatus(self):
         pass
         
    def displayBookInfo(self):
        print("Book Information:")
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"Year: {self._yearPublished}")
        
class AvailableBook(Book):
     def displayStatus(self):
        print("Status: Available")
class ReservedBook(Book):
     def displayStatus(self):
        print("Status: Reserved")
class BorrowedBook(Book):
     def displayStatus(self):
        print("Status: Borrowed")
class Main:
    def main():
        option=int(input("Enter your option (1-3): ").strip())
        match(option):
            case 1:
                
                title=input("Enter book title: ")
                author=input("Enter book author: ")
                year=int(input("Enter year published: "))
                obj=AvailableBook(title, author, year)
                obj.displayBookInfo()
                obj.displayStatus()
            case 2:
                
                title=input("Enter book title: ")
                author=input("Enter book author: ")
                year=int(input("Enter year published: "))
                obj=ReservedBook(title,author,year)
                obj.displayBookInfo()
                obj.displayStatus()
            case 3:
                title=input("Enter book title: ")
                author=input("Enter book author: ")
                year=int(input("Enter year published: "))
                obj=BorrowedBook(title,author,year)
                obj.displayBookInfo()
                obj.displayStatus()
            case _:
                print("Invalid option! Please enter 1, 2, or 3.")
                return
Main.main()
