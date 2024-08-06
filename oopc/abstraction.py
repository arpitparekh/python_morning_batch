# abstraction
# कोई सामान्‍य धारणा जिसका आधार कोई वास्‍तविक व्‍यक्ति, वस्‍तु या स्थिति न हो
# khayali pulav

# abstract class

from abc import ABC, abstractmethod

# you can not create object of an abstract class

class Boss(ABC):                             # abstract class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @abstractmethod        # method without any body
    def work(self):
        pass
    
    @abstractmethod        # method without any body
    def timepass(self):
        pass
    
    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Employee(Boss):
    def __init__(self, name, salary, emp_id):
        super().__init__(name, salary)
        self.emp_id = emp_id
        
    def work(self):
        print(f"{self.name} is working")
        
    def timepass(self):
        print(f"{self.name} is time passing")   
        
# abstract class is used to provide implementation to another class        

e = Employee("Pradip",1000,12)
e.work()
e.timepass()
                

        