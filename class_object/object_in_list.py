class Car:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand
    
    def __str__(self) -> str:
        return f"Name is {self.name} Brand is {self.brand}"        

# c1 = Car("s1","bmw")

carList = [Car("s1","bmw"),Car("figo","ford")]

for x in carList:
    print(x.name)
    print(x.brand)
    
                