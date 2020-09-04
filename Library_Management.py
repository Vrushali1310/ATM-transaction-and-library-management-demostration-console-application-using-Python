class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Library is updated. You can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print("Book has been added to the book list")

    def returnBook(self,book):
        self.booklist.remove(book)

vrushali = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics \n'],"CodeWithHarry")

while(True):
    print("Welcome to the Vrushali's Library. ")
    print("1. Display Books \n2. Lend a Book \n3. Add a Book")
    user_choice = int(input("Enter your choice to continue : "))

    if user_choice == 1:
        vrushali.displayBooks()
    elif user_choice == 2:
        user = input("Enter your name : ")
        book = input("Enter the name of the book you want to lend :")
        vrushali.lendBook(user, book)
    elif user_choice == 3:
        book = input("Enter the name of the book you want to add :")
        vrushali.addBook(book)
    elif user_choice == 4:
        book = input("Enter the name of the book you want to return :")
        vrushali.returnBook(book)
    else:
        print("Not a valid option")

    
    user_choice2 = input("Press c to continue and q to quit : ")  
    if(user_choice2 != 'c' and user_choice2 != 'q'):
        user_choice2 = input("Please enter valid choice")
    elif (user_choice2 == 'q'):
        quit()
    else:
        continue

