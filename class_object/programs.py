# You're developing a simple banking system. 
# Create a BankAccount class with methods for deposit, withdrawal, and checking balance. 
# Then, create a SavingsAccount subclass that has an additional interest rate 
# attribute and a method to apply interest. 
# How would you implement this?

class BankAccount:
    def __init__(self, deposit,withdrawl):
        self.deposit = deposit
        self.withdrawl = withdrawl
        self.balance = deposit-withdrawl
        
class SavingAccount(BankAccount):
    
    def __init__(self, deposit,withdrawl,interest_rate):
        # calling parent class contructor in child class
        super().__init__(deposit,withdrawl)                  
        self.interest_rate = interest_rate
    
    def applyIntrest(self):
        self.balance = self.balance * self.interest_rate
    
    def display(self):
        print("Deposit: ",self.deposit)
        print("Withdrawl: ",self.withdrawl)
        print("Interest Rate: ",self.interest_rate)
        print("Balance: ",self.balance)

s1 = SavingAccount(2000,1000,1.2)
s1.applyIntrest()
s1.display()


# Design a basic e-commerce system with a Product class and a ShoppingCart class. 
# The ShoppingCart should be able to add products, remove products, 
# and calculate the total price. How would you implement these classes and their 
# interactions?

class Product:
    
    products = []
    
    def __init__(self, product):
        self.products.append(product)
        
    def display(self):
        print(self.products) 


class ShoppingCart(Product):
    def __init__(self, name, price, quantity):
        super().__init__([name,quantity,(price*quantity)])
    
    def addProduct(self,name, price, quantity):
        self.products.append([name,quantity,(price*quantity)])
    
    def removeProduct(self,name):
        for x in self.products:
            if x[0] == name:
                self.products.remove(x)


s1 = ShoppingCart("Tissue",20,200)
s1.addProduct("Shoes",2,1000)
s1.display()
s1.removeProduct("Tissue")
s1.display()
        