# Define classes for Person, Student, Professor, and Course.
# Implement inheritance and composition where necessary.
# Include methods for enrolling students, assigning professors to courses, 
# and calculating average grades.

class Person:
    
    def __init__(self, name, age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
class Professor(Person):
    
    def __init__(self, name, age, gender,professor_name):
        self.professor_name = professor_name
        Person.__init__(self,name, age, gender)        
        
class Course(Professor):
    
    course_name = []
    
    def __init__(self, course_id = 0, course_name = "", credits = 0,name="", age=0, gender="",professor_name=""):
        
        super().__init__(name, age, gender,professor_name)
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits


class Student(Course):
    
    marks = []
    average_marks = 0
    
    def __init__(self, name, age, gender,course_id,no_course, course_name, credits,enroll_id,marks,professor_name):
        
        self.no_course = no_course
        self.marks = marks
        self.enroll_id = enroll_id
        Course.__init__(self,course_id, course_name, credits,name, age, gender,professor_name)
        
    def findAverageMarks(self):
        sum = 0
        for x in self.marks:
            sum += x
        
        return (sum)/self.no_course
    
    def display(self):
        print("Student Name : ",self.name)
        print("Student Age : ",self.age)
        print("Student Gender : ",self.gender)
        print("Course ID : ",self.course_id)
        print("Course Name : ",self.course_name)
        print("Credits : ",self.credits)
        print("Enroll ID : ",self.enroll_id)
        print("No of Courses : ",self.no_course)
        print("Name of Professor : ",self.professor_name)
        print("Marks : ",self.marks)
        print("Average Marks : ",self.findAverageMarks())
        
course_name = []
marks = []
credit = []


no_of_course = int(input("Enter No Of Course : ")) # 5
for x in range(1,no_of_course+1):
    course_name.append(input("Enter Course Name : "))
    marks.append(int(input("Please Enter Marks : ")))
    credit.append(int(input("Please Enter Credit : ")))

student = Student(
    input("Enter Name : "),
    int(input("Enter Age : ")),
    input("Enter Gender : "),
    int(input("Enter Course Id : ")),
    no_of_course,course_name,credit,int(input("Enter Enroll Id : ")),marks,input("Enter ProfesorName : "))
student.display()
        

        