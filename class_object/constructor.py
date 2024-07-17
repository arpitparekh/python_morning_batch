class Vehicle:
    
    company_name = ""
    model_name = ""
    milege = 0
    no_seat = 0
    
    # constructor is a type of funciton
    # constructor is used to create an object of a class
    # constructor calls automatically when we create an object of class
    
    def __init__(self,name):
        print(f"Constructor is calling hi {name}")             
  
v = Vehicle("Kevin")