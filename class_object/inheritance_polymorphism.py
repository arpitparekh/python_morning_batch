class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self,a,b):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("values are",a,b)

class Child(Parent):
    def __init__(self, name, age, school):
        super().__init__(name,age)
        self.school = school
    
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("School: ", self.school)


c1 = Child("Pintu",8,"Balbharti Vidhyabhavan")
c1.display()

p1 = Parent("Bhavin",45)
p1.display(12,13)


        