class A:
    # part of a class
    number = 34   # static members
    
    def __init__(self,x):
        self.x = x     # local members
    
    def display(self):
        print("x :",self.x)
        print("number : ",A.number)
    
    @classmethod    
    
    # binding of a function to
    # class
    
    def fun(cls,a):
        print("a : ",a)
        

a  = A(12)        
a2 = A(13)
a3 = A(15)

a.display()
a2.display()
a3.display()

A.number = 45

a.display()
a2.display()
a3.display()


A.fun(12)

# oopc
# class
# object
# constrcutor
# class methods(function)
# inheritance
# encapsulation
# polymorphism
# abstrction
# static memebers


