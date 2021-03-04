class Student:
    def __init__(self, student_List):
        self.student_List = student_List

    def borrow_Book(self):
        req_book = input("Enter the name of the book you want to borrow: ")
        req_book = req_book.upper()
        return req_book

    def return_Book(self):
        return_book = input("Enter the name of the book you want to return/add: ")
        return_book = return_book.upper()
        if return_book in student_List:
            print("Thanks! I hope you enjoyed readying this book.")
            student_List.remove(return_book)
            return return_book
        else:
            print(f"Thanks for donating {return_book} book")
            return return_book 

class Library(Student):
    def __init__(self, books):
        self.books = books
        # print(self.books

    def display_Books(self):
        print("The available books in Library: ")
        for book in self.books:
            print("*", book)

    def borrow_Book(self, book_Name):
        if book_Name in self.books:
            print(f"You have been issued {book_Name}, Please return it within 7 days!")
            self.books.remove(book_Name)
            student_List.append(book_Name)
            print(student_List)
        else:
            print("This book is either unavailable or already been issued to someone else.")

    def return_Book(self, book_Name):
        self.books.append(book_Name)


if __name__=="__main__":
    student_List = []
    book_List = ["Python", "Django", "Flask", "Statistics", "Machine Learning"]
    book_List = list(map(lambda x : x.upper(), book_List))
    welcomemsg = '''\n********* Welcome to the Central Library ********* 
    1. Display the book_List
    2. Request a book
    3. Return/Add a book
    4. Exit\n'''
    central_Library = Library(book_List)
    Stu_obj = Student(student_List)

    while(True):
        print(welcomemsg)
        choose = int(input("Please choose the option: "))
        if(choose == 1):
            central_Library.display_Books()
        elif(choose == 2):
            central_Library.borrow_Book(Stu_obj.borrow_Book())
        elif(choose == 3):
            central_Library.return_Book(Stu_obj.return_Book())
        elif choose == 4:
            print("Thanks for using Central Library")
            exit()
        else:
            print("Invalid Entry! Please try again..")
      

