# object class
# parent class of all the class in python

class A(object):
    
    def __init__(self):
        print("Class A Constructor")
        
class B(object):
    
    def __init__(self):
        print("Class B Constructor")        
        

class C(A,B):
    def __init__(self): 
        B.__init__(self)    # explicit parent constructor call  
        A.__init__(self)    # explicit parent constructor call       
        
c = C()        
    
# object is a kind of placeholder, 
# letting Python know you don’t want to inherit the properties of some other class. 
# You’re making a class with the very basic rules
# and your code will set up everything else.

# Abstract
# Encapsulation
# Iterators