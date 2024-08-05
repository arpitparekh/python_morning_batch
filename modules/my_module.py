# python module
# modules are just same as python code
# hello() => in different file

def jumping():
    print("I am jumping")
    
    
class Person:
    def __init__(self, name):
        self.name = name     
        
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}           

def findPrime(a):   # 23  
    if a <= 1:
        return False
    
    for i in range(2,a):    # 2..22
        if a%i==0:
            return False
        
    return True