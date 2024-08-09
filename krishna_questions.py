# Basic Inheritance:

# Task: Create a base class Animal with a method speak that prints "Animal speaks". 
# Then, create a derived class Dog that overrides the speak method to print" "Dog barks". 
# Demonstrate the usage of both classes.


class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
     def speak(self):
        print("Dog barks")  

d = Dog()
d.speak() 

# Multiple Inheritance:

# Task: Create two base classes, FlyingAnimal with a method fly that prints "Flying" 
# and SwimmingAnimal with a method swim that prints "Swimming". 
# Then, create a derived class Duck that inherits from both FlyingAnimal and SwimmingAnimal. 
# Demonstrate the usage of the Duck class.



# Super Keyword:

# Task: Create a base class Vehicle with an init method that initializes make and model. 
# Then, create a derived class Car that also initializes number_of_doors. 
# Use the super keyword to call the Vehicle's init method from the Car class.

class Vehicle:
<<<<<<<<<<<<<<  ✨ Codeium Command 🌟 >>>>>>>>>>>>>>>>
    def __init__(self, make, model):
        if make is None or model is None:
            raise ValueError("Make and model must not be None")
    def __init__(self, make, model):           # constrcutor
        self.make = make
        self.model = model
<<<<<<<  a27b3773-c697-436c-81d3-0793961835de  >>>>>>>
    
class Car(Vehicle):
    def __init__(self,no_of_doors,make, model):
        super().__init__(make, model)
        self.no_of_doors = no_of_doors
    
    def display(self):
        print(f"Make: {self.make}, Model: {self.model}, Number of Doors: {self.no_of_doors}")

c = Car(4,"BMW","M3")
# print(c.make)
# print(c.model)
# print(c.no_of_doors)
c.display()
    


        
    
            
    
