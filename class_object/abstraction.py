# abstraction
# making it abstract
# existing only as an idea, not as a physical thing
# to hide someting
# class is a blueprint
# abstract class is a blueprint for other classes

# abstract class can have all the functionality of normal class
# abstract class can have abstract methods

# abstract methods are the methods without any body


from abc import ABC, abstractmethod
from typing import override

class Polygon(ABC):
    
    no_of_sides = 0
    
    # abstract method
    
    @abstractmethod                       
    def print_sides(self):
        pass
    
    @abstractmethod                       
    def print_angles(self):
        pass
    
    @abstractmethod                       
    def print_area(self):
        pass
        
    def display(self,a):
        print("Display method from parent class")    
    
class Triangle(Polygon):
    
    def print_sides(self):
        print("I have 3 sides")

    def print_angles(self):
        print("I have 3 angles")
        
    def print_area(self):
        print("area is falana dhikna")        
    
    def display(self,a):
        print("Display method from child class")      
        

# p = Polygon()  # you can not create an object of abstract class

t = Triangle()
t.print_sides()
t.print_angles()
t.print_area()
t.display(12)
    

