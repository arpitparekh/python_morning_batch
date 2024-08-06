class Shape:
    
    shape=""
    angle =0

    def assignValues(self,shape,angle):  # assigning a prierties value using function
        self.shape = shape
        self.angle = angle

    def printValues(self):
        print("Shape is",self.shape)   
        print("Shape is",self.angle)      


s = Shape()
s.assignValues("Circle",0)
s.printValues()

s1 = Shape()
s1.assignValues("Rectangle",4)
s1.printValues()
s1.assignValues("Triangle",3)

s1.printValues()
