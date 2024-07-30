# encapsulation
# is protecting a variables and function
# to hide something inside a capsule

# oopc
# class
# object # instance
# method
# attribute # variables
# encapsulation
# abstraction
# inheritance
# polymorphism

from abc import ABC

class Demo(ABC):
    
    def display(self):
        pass



class A:
    
    def abc(self):
        print("a")
        
class B(A):                     # method oervlaoding
    
     def abc(self,a):
        if(a):
            print("b")
        else:
            A.abc(self)
        
b = B()
b.abc(False) 


# a = A()
# a.abc()   


# still pending

#_a
#__a

# put data and function inside a capsule to hide them from outer access

class Building:
    
    max_length= 50
    
    def __init__(self,name):
        self._name = name               # protected variable of class
    
    def display(self):
        print(self._name)
    
    # we can access protedt variable outside of a class        
    
class Parking(Building):
    
    def __init__(self, name):
        super().__init__(name)
    
    def display(self):
        print(self._name)           # we can access  proteced member in child class
        
    

b = Building("Indraprasth")
b.display()
print(b._name)
p = Parking("Vidheshwar")
p.display()
print(p._name)


class Warehouse:
    
    def __init__(self,size):
        self.__size = size   # private member of a class
        pass
    
    
    def display(self):
        print(self.__size)
        
    def assign(self,size):
        self.__size = size        
    
        
    def __calculate(self):                           # private function
        return "This is retuning string"
    
    
    
class Cabin(Warehouse):
    
    def __init__(self, size):
        super().__init__(size)
        
    def display(self):
        print(self.__size)        
    

w = Warehouse(30)

w.display()

c = Cabin(55)
# c.display()

# c.__calculate()
w.__calculate()


        
        
      
        
    

            
       

