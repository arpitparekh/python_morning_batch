class A:
    
    def __init__(self,number):
        self.number = number


class B(A):
    
    def __init__(self,value):
        self.value = value
        super().__init__(value*100)
        
b = B(66)
print(b.value)
print(b.number)

b = B(68)
print(b.value)
print(b.number)        