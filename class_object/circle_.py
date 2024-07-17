class Circle:
    
    def findCircumference(self):
        self.circum = 2 * 3.24 * self.radius
    
    def __init__(self,radius):
        self.radius = radius
    
    def findArea(self):
        self.area = 3.14 * self.radius * self.radius
        
    area = 0
    circum = 0
    
    # def display(self):
    #     print(f"Radius is {self.radius} and area is {self.area} and circumference is {self.circum}")
        

c = Circle(15)
c.findArea()
c.findCircumference()
# c.display()

print(c.radius)
print(c.area)
print(c.circum)



        
