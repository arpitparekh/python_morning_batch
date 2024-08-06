# veriables
# datatypes
# operators
# conditional statements
# loop
# loop inside loop
# function
# lambda function

# class objects
# constructor
# polymorphism
# abstraction
# Inheritance
# Encapsulation
# inner class
# static methods
# Super()

# module, packages and import
# regex

# sql
# file handling
# exception Handling

# GUI
# numPy
# pandas


# class and objects
# class is a blueprint
# class is collection of atributes//variables and functions//methods
# class should always be capital


def name(a):  # empty function
    pass

name(12)

class College:   # empty class
    pass

class Student:

    a = 12
    b = 13

    def display(self):   # we must have to pass self in function arguments when we make it insdie a class
        print("This is display method")
        print(self.a)                         
        print(self.b)   # class object is denoted by self inside a class

# to access class properies and functions we need object
# object is an instance of class

s = Student()
s1 = Student()

s.display()
s1.display()

s.a = 55
s.b = 66

s.display()
s1.display()







