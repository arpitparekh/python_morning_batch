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

class A:
    
    def abc(self):
        print("a")
        
class B(A):
    
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
        
        
      
        
    

            
       

