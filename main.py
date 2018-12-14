# Objects missing
# Author, etc some other classes were also there
from inventory import Inventory
from user import User
from author import Author
def main():

    k = {"The Miracle": {'author': 'A', 'price': 234, 'copies': 50},
         "The Cluster": {'author': 'A', 'price': 234, 'copies': 50},
         "The Awakening": {'author': 'A', 'price': 234, 'copies': 50},
         "The Mindset": {'author': 'B', 'price': 234, 'copies': 50}}
    var=True
    book1 = Inventory(k)
    user1 = User(k)
    author1 = Author(k)
    while var: # Extremely wrong, in terms of OOP, never write code outside classes
    # Too much complicated logic in one code block, needs multiple functions for it
        print("To Login as admin Enter 1")
        print("To Login as user Enter 2")
        print("To Exit Enter 3")
        win=input("Please enter your option: ")
        if win == 1:
            print("To add Book Enter 1")
            print("To display Book Inventory  Enter 2")
            tty=input("Please enter your option: ")
            if tty == 1:
                name=input("Enter the name of the book: ")
                copies=input("Enter the no of the book copies to be added: ")
                book1.add_Book(name, copies)
            elif tty == 2:
                book1.disp_Invent()
        elif win == 2:
            print("To order Book Enter 1")
            print("To rate a Book Enter 2")
            print("To list the Books by an author Enter 3")
            print("To list the no of copies sold for a Book Enter 4")

            tty1=input("Please enter your option: ")
            if tty1 == 1:
                name=input("Enter the name of the book: ")
                copies=input("Enter the no of the book copies to be ordered: ")
                user1.order_Book(name, copies)
            elif tty1 == 2:
                name=input("Enter the name of the book: ")
                print("For Five star rating Enter 1")
                print("For Four star rating Enter 2")
                print("For Three star rating Enter 3")
                print("For Two star rating Enter 4")
                print("For One star rating Enter 5")
                rating=input("Enter the rating: ")
                user1.rating_Book(name, rating)
            elif tty1 == 3:
                author=input("Enter the name of the author: ")
                author1.list_Book(author)                
            elif tty1 == 4:
                name=input("Enter the name of the book: ")
                user1.display_Order(name)
        elif win == 3:
            break

if __name__ == '__main__':
    main()

