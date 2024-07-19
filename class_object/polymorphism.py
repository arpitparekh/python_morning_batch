# polymorphism in python
# polymorphism means one name many forms

# parameter have to be different

# function without any class

# def display(a):
#     print("value is",a)
    
# def display():
#     print("Hello")
    
def display(a,b):
    print("values are",a,b)
        
display(12,13)

list = [1,2,3,4,5]
name = "Bascom"

print(len(list))
print(len(name))    

# polymorphic function
# works same in multiple condition

def sum(a=0,b = 0,c = 0):   # user define polymorphic function
    print(a+b+c)
    
# here polymorphism is achived using different parameters and defual vales   
    
sum(12)    
sum(12,13)    
sum(12,13,14)    # more then one form

class College:
    
    def study(self):
        print("study")
    
    def teaching(self):
        print("teaching")

class School:
    
    def study(self):
        print("study")
    
    def teaching(self):
        print("teaching")
            
c1 = College()
s1 = School()

# we can also achive polymorphism using same name fucntion in different class

# c1.study()
# s1.study()
# c1.teaching()
# s1.teaching()

for objects in (c1,s1):
    objects.study()
    objects.teaching()