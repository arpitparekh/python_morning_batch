class College:
    name = ''
    no_student = 0

    def display(self):                  # function that display the proerties of an object
        print("Name is",self.name)
        print("No of Student is",self.no_student)

    # binding of variables an fucntion inside a class    

c = College()

c.name = "L.D. Engineering"
c.no_student = 200

c.display()

c1 = College()

c1.name = "Ahmedabad University"
c1.no_student = 150

c1.display()



