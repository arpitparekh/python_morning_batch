# class is blueprint
# class is a collection of variables and methods

# Student
# height id roll no name

    
class Student:
    
    roll_no = 12    # property # data members # variables 
    height = 12.4
    name = "karan"
    list=[1,2,4,5]
    reviews=[]
       
    def display():   # methods  # member function
        print("Display method")

s = Student()
s.roll_no = 12
s.height = 34.45
s.name="Sapan"

print(s.roll_no)
print(s.height)
print(s.name)
s.display()

s1 = Student()
s1.roll_no = 13
s1.height = 34.65
s1.name="Rachana"

print(s1.roll_no)
print(s1.height)
print(s1.name)
s1.display()