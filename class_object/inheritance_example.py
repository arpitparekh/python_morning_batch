# Write a Python class called "Rectangle" that inherits from a class called "Shape". 
# The "Shape" class has attributes "color" and "area", 
# and the "Rectangle" class has attributes "length" and "width". 
# Create an object of the "Rectangle" class and print its color, area, length, and width.

class Shape:
    def __init__(self, color,area):
        self.color = color
        self.area = area

class Rectangle(Shape):  # rectangle class is child of shape class
    
    def __init__(self, color,length, width):
        
        # calling parent class constuctor from child class
        super().__init__(color,self.findArea(length,width))                   
        
        self.length = length
        self.width = width
    
    def findArea(self,l,w):
        return l*w        

    def __str__(self):
        return f"color: {self.color}\narea: {self.area}\nlength: {self.length}\nwidth : {self.width}"
                
r1 = Rectangle("Red",12.34,3.45)
print(r1)
