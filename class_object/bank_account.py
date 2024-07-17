# Design a BankAccount class with fields for accountNumber, accountHolderName and balance. 
# Write a constructor to initialize these fields. 
# Include methods to deposit, withdraw, and check the balance. 
# Create objects of BankAccount and perform some transactions.

class BankAccount:
    
    def __init__(self, accountNumber, accountHolderName, balance):
        self.accountNumber = accountNumber
        self.accountHolderName = accountHolderName
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully")
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} withdraw successfully")
    
    def checkBallance(self):
        print(f"Balance is {self.balance}")
        
    def __str__(self):
        return f"Account Number: {self.accountNumber}\nAccount Holder Name: {self.accountHolderName}\nBalance: {self.balance}"
    

b1 = BankAccount(123456789,"Rahul",10000)

print()

b1.deposit(1000)   # perform some transaction
b1.withdraw(500)
b1.checkBallance()

print(b1)

            
                
            
    
            