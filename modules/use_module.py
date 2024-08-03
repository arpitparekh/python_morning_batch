# from my_module import Person,jumping,data

import my_module as m  # renaming a module

m.jumping()

class Student(m.Person):
    def __init__(self, name):
        super().__init__(name)

print(m.data)