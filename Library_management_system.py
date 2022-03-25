class Student:

    def requestBook(self):
        self.book = input("Enter the name of book you want to borrow.\n")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of book you want to return back.\n")
        return self.book

class Library:
    def __init__(self, listOfBook):
        self.books = listOfBook

    def displayAvailableBooks(self):
        print("Currently Available Books are :")
        for book in self.books:
            print("*" + book)

    def borrowBook(self, book):
        if book in self.books:
            print(
                f"Thanks for using our Library System. Book {book} has been alloted to you, so Please return it within 30 days.")
            self.books.remove(book)

    def returnBook(self, book):
        self.books.append(book)
        print("Thanks for using our Library System and submitting the book {} on time".format(book))


if __name__ =="__main__":
    obj_Lib = Library(["c", "Java", "python", "ML"])
    obj_Stu = Student()
    while True:
        welcome_msg = '''
        ==== Welcome to AEC Library Management System ====
        Choose the below optinons:
        Enter 1 for listdown the available books
        Enter 2 for withdrawal process of book
        Enter 3 for returning process of book
        enter 4 for Exit
        '''
        print(welcome_msg)
        key = int(input("Enter your desire key\n"))
        if key == 1:
            obj_Lib.displayAvailableBooks()
        elif key == 2:
            obj_Lib.borrowBook(obj_Stu.requestBook())
        elif key == 3:
            obj_Lib.returnBook(obj_Stu.returnBook())
        elif key == 4:
            print("Thanks for visiting our AEC library system. Have a nice day!")
            exit()
        else:
            print("You have entered Invalid key")

    # # print(obj_Lib.books)
    # obj_Lib.displayAvailableBooks()
    # obj_Lib.borrowBook(obj_Stu.requestBook())
    # obj_Lib.displayAvailableBooks()
    # obj_Lib.returnBook(obj_Stu.returnBook())
    # obj_Lib.displayAvailableBooks()
