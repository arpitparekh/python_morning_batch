# constructor
# constructor is used to make an object(instance) of class
# constrcutor is a type menthod that calls automatically when we create an instanec of a class


class Institute:
    
    # def __init__(self):                     # default constructor
    #     print("Calling Constrcutor")
    
    def __init__(self,init_name,no_student,no_chair,no_teachers,rating):
        self.inst_name = init_name
        self.no_student = no_student
        self.no_chair = no_chair
        self.no_teachers = no_teachers
        self.rating = rating
    
    def display(self):
        print("Institute Name : ",self.inst_name)
        print("No of Student  : ",self.no_student)
        print("No of Chair    : ",self.no_chair)
        print("No of Teachers : ",self.no_teachers)
        print("Rating         : ",self.rating)
    

i = Institute("Bascom",30,50,6,3.9)
i.display()

i2 = Institute("Tops",100,20,15,3.5)
i2.display()
