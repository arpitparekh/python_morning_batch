class Bank:
    name = ""
    address = ""
    credit = 0
    debit = 0
    balance = 0
    
    def assignValue(self,name,address,debit,credit):
        self.name = name
        self.address = address
        self.debit = debit
        self.credit = credit
        self.balance = self.debit - self.credit
    
    def display(self):
        # display values
        print("Name : ",self.name)
        print("Address : ",self.address)
        print("Balance : ",self.balance)
    
    def creditAmount(self,credit):
        if self.balance-credit<0:
            print("Insufficient Balance")
        else:
            self.balance = self.balance-credit  
    
    def debitAmount(self,debit):
        self.balance = self.balance+debit
        
# डेबिट प्रविष्टि हमेशा खाता बही में एक सकारात्मक संख्या जोड़ती है, और क्रेडिट प्रविष्टि हमेशा एक नकारात्मक संख्या जोड़ती         

b = Bank()
b.assignValue("HDFC","Vastrapur",20000,6000)
b.display()
b.creditAmount(5000)
b.display()
b.creditAmount(7000)
b.display()
b.creditAmount(3000)
b.display()
b.debitAmount(3000)
b.display()
b.creditAmount(3000)
b.display()

b1 = Bank()
b1.assignValue("AXIS","Maninagar",10000,0)
b1.display()
    