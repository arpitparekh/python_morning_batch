# single level

class A:
    pass
class B(A):
    pass

# multi level

class College:
    
    def __init__(self,col_name,address):
        self.col_name = col_name
        self.address = address
        
class Student(College):
    
    def __init__(self, name,roll_no,col_name,address):
        
        super().__init__(col_name,address)     # with the use of super we can call parent class constructor in child class constrcutor
        self.name = name
        self.roll_no = roll_no        

class Library(Student):
    
    def __init__(self, name, roll_no, col_name, address,book_name,return_date):
        self.book_name = book_name
        self.return_date = return_date
        super().__init__(name, roll_no, col_name, address)
        
    def display(self):
        print("College Name is : ",self.col_name)
        print("Address is : ",self.address)
        print("Name is : ",self.name)
        print("Roll no is : ",self.roll_no)
        print("BookName is : ",self.book_name)  
        print("Return Date is : ",self.return_date)    
        
l = Library("Majnu Bhai",420,"Uday Shetty Institute of Weponary","Vassepur","how to flirt with a girl","no return")
l.display()




    

        
    
    
