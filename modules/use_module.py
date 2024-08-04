# from my_module import Person,jumping,data

# import my_module as m # renaming a module

from my_module import jumping,Person,data,findPrime

jumping()

class Student(Person):
    def __init__(self, name):
        super().__init__(name)

print(data)
        
print(findPrime(23))