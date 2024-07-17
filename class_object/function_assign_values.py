class College:
    
    # oopc
    # object oriented programming concept
    
    name = ""
    no_students = 0
    no_bench = 0
    no_departments = 0   # default values of the object
    
    def assignValues(self,name,no_students,no_bench,no_departments):
        
        # i'm assigning parameter values to class properties

        self.name = name
        self.no_students = no_students
        self.no_bench = no_bench
        self.no_departments = no_departments
        
    def displayFunction(self):
        print(self.name) 
        print(self.no_students)      
        print(self.no_bench)      
        print(self.no_departments)           
        
# we can represent class object inside a class using self     

c = College()      
c1 = College()
#c.name = "ADIT"
#c.no_students = 400
#c.no_bench = 500
#c.no_departments = 8

c.assignValues("Adit",400,500,8)          # way 1 to assign values
c1.assignValues("LJ",500,45,10)

c.displayFunction()
c1.displayFunction()

print(c)  # it displays the object location in memory



def display():
    return 12


