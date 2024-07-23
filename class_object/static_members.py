# static members
# static members inside a class are belongs to the clss itself but not to a objects

class Travel:
    # static members
    # no_of_travelers = 0  # property
    
    mode_of_transport = "Car"  # static member  # class variable
    
    def __init__(self,no_of_travelers,destination):
        self.no_of_travelers = no_of_travelers
        self.destination = destination
    
    def display(self):
        print("No of travelers are: ",self.no_of_travelers) # functions
        print("Destination is : ",self.destination) # functions
        print("Mode of Transport is : ",Travel.mode_of_transport) # functions
        
    # inside a static function we can only access static variables
    # use of static method is to access static variable and do some action on it    
       
    @classmethod    
    def fun(cls,mode_of_transport):
        print("This is a static function")
        cls.mode_of_transport = mode_of_transport
        

# class properties
# class methods
# class constructors        

t1 = Travel(12,"Jaipur")
t1.display()

Travel.mode_of_transport = "Train"

t2 = Travel(14,"Udaipur")
t2.display()

t3 = Travel(56,"Jammu")
t3.display()

Travel.fun("Plane")   # we change a static variable value using a static function

t4 = Travel(2,"Nal Sarovar")
t4.display()




    