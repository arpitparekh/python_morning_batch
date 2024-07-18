# inheritance
# inherit (varso)

# inheritance allows us to define a class that 
# inherit methods and properties from another class

class Person:
    def __init__(self, name, age,isMale):
        self.name = name
        self.age = age
        self.isMale = isMale                        
        
    def __str__(self):
        return f"Name is : {self.name}\nAge is: {self.age}\nGender : {"Male" if self.isMale else "Female"}"        

p1 = Person("Jimit",23,True)
print(p1)

class Student(Person):  # defination class  # pass parent class in ()
    # pass                # bypass th error using pass keyword
    
    def __init__(self,name, age,isMale,course_name):
        super().__init__(name,age,isMale)              # super method class the parent class constructor
        self.course_name = course_name
    
    def __str__(self):
        return f"Name is : {self.name}\nAge is: {self.age}\nGender : {"Male" if self.isMale else "Female"}\nCourse Name : {self.course_name}"        
        
        
s1 = Student("Rajana",25,False,"Python Course")
print(s1)
