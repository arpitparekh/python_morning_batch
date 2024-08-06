# Create an Abstract Class for Shapes
# that has an abstract method called area(). 
# Then, create subclasses for Circle, Rectangle, and Triangle that implement the area() method. 
# What would the implementation look like?

from abc import ABC, abstractmethod


class Shapes(ABC):
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print(self.radius*self.radius*3.14)

        
c = Circle(12.34)
c.area()
               