class Bascom:
    # id = 0
    # no_student = 0
    # head_name = ""
    # branch_name = ""
    
    # constructor
    # is a function that calls automatically when we create an object of that class
    
    
    # def __init__(self):
    #     print("This is Constructor")
        
    def __init__(self,id,no_student,head_name,branch_name):
        self.id = id
        self.no_student = no_student
        self.head_name = head_name
        self.branch_name = branch_name      
        
    # inside a class class object is annoted with self keyword        
    
    # def assignValues(self,id,no_student,head_name,branch_name):
    #     self.id = id
    #     self.no_student = no_student
    #     self.head_name = head_name
    #     self.branch_name = branch_name
        
    def displayValues(self):
        print("id = ",self.id)
        print("no_student = ",self.no_student)
        print("head_name = ",self.head_name)
        print("branch_name = ",self.branch_name)

# b = Bascom()
# b.assignValues(12,10,"Rahul","CSE")

# b1 = Bascom()
# b1.assignValues(13,15,"Pranav","Vastrapur")

# b.displayValues()
# b1.displayValues()

# b.id = 12
# b.no_student = 10
# b.head_name = "Rahul"
# b.branch_name = "CSE"

# b2 = Bascom(66,67,"BHavya","Maninagar")
# b2.displayValues()

b3 = Bascom(77,78,"Bhuvan","Jamalpur")
b3.displayValues()