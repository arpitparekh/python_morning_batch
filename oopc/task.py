# Basic Inheritance:
# Create a base class Animal with a method speak that prints "Animal speaks". 
# Then, create a derived class Dog that overrides the speak method to print "Dog barks". 
# Demonstrate the usage of both classes.

class Animal:
    
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    
    def speak(self):           # override
        print("Dog barks")
        
d = Dog()
d.speak()        


# Multiple Inheritance:
# Create two base classes, FlyingAnimal with a method fly that prints "Flying" 
# and SwimmingAnimal with a method swim that prints "Swimming". 
# Then, create a derived class Duck that inherits from both FlyingAnimal and SwimmingAnimal. 
# Demonstrate the usage of the Duck class.

class FlyingAnimal:
    
    def fly(self):
        print("Flying")

class SwimmingAnimal:
    
    def swim(self):
        print("Swimming")

class Duck(FlyingAnimal,SwimmingAnimal):    # multiple inheritance
    pass

d = Duck()
d.fly()
d.swim()  

# Super Keyword:
# Create a base class Vehicle with an init method that initializes make and model. 
# Then, create a derived class Car that also initializes number_of_doors. 
# Use the super keyword to call the Vehicle's init method from the Car class.

class Vehicle:
    
    def __init__(self,make,model):
        self.make = make
        self.model = model

class Car(Vehicle):
    
    def __init__(self,no_of_doors,make,model):
        super().__init__(make,model)
        self.no_of_doors = no_of_doors
        
    
    def display(self):
        print(f"make is {self.make} model is {self.model} no of door is {self.no_of_doors}")
        
        

c = Car(4,"Maruti","300")
c.display()

        
        
            
        
        
