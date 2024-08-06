# encapsulation
# capsul k angar bundh kar dena

class Student:
    def __init__(self, name, age, marks):
        self.__name = name
        self.__age = age
        self.__marks = marks   # private members
    
    def display(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"marks: {self.__marks}")
        self.__fun()
        

    def __fun(self):
        print("This is private function")
        
        

s = Student("Pradip",34,45)
s.display()

# s.__fun()   # this is private function

# print(s.__name)  # we can't access it using an object


        


