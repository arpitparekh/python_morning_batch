# Errors are problems in a program due to which the program will stop the execution. 
# On the other hand, exceptions are raised when some internal 
# events occur which change the normal flow of the program. 

# syntax error
# print("hello"

# type error
# print("hello" + (5))

# name error
# prit("Hello")

# IndexError
# list = [12,3,56,4,34]
# print(list[6])

# dictionary

# KeyError
# person = {
#     "name":"bascom",
#     "no_of_student":20
# }

# print(person["chair"])

from decimal import DivisionByZero


def display(a : int):
    print(a)

display(12)
# display("Bascom")
# display(12.13)


# ValueError: This exception is raised when a function or method 
# is called with an invalid argument or input, 
# such as trying to convert a string 
# to an integer when the string does not represent a valid integer. 

# num = int(input("Please Enter Number : "))    #  "12122122" 
# print(num)

# AttributeError
class Demo:
    def __init__(self,value):
        self.value = value

d = Demo(12)
# print(d.age)

# ZeroDivisionError
# print(12/0)

# ModuleNotFoundError
# import my_moduley


# 501 , 502


a = int(input("Please Enter Number : "))
b = int(input("Please Enter Number : "))

# handling and Error before is arrives

try:
    print(a/b)
    print(d.age)
    print("Hello")
    
# except ZeroDivisionError:
#     print("Zero Se divide ki error ayi hee")
# except AttributeError:
#     print("AttributeError ayi hee")
except:
    print("Error Ayi he")
else : 
    print("No Error Ayi hee")
finally :
    print("This is finally block")     #  it will run every time whether error is there

print("Hello")

# raise an exception

try:
    print("Hello")
    
    raise KeyError("Bhai ye mene raise ki he")
    
except:
    print("Error Ayi hee")
        