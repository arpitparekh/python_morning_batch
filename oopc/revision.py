# oopc
# class
# properties , variables, atributes
# methods , function
# constrcutor


# object

# inheritance # varso
# one class can use properties and methods of another class
# we can resuse class property and methods


class Parent():
    
    def __init__(self,firstName,lastName,age,birthDate):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.birthDay = birthDate
    
    def display(self):
        print(self.firstName)
        print(self.lastName)
        print(self.age)
        print(self.birthDay)

class Child(Parent):  # child parent ko apneme inherit kar raha he
    pass

c = Child("pintu","patel",26,"12-03-1998")
c.display()

p = Parent("paresh","patel",55,"12-04-1843")
p.display()

