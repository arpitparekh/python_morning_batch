# decimal to binary conversion
# logic
# 1234
# 1234 % 2   = 0
# 1234 // 2  = 617
# 617 % 2    = 1
# 617 // 2   = ...

n = int(input("Enter Decimal number : "))
original = n
binary = ""                 # empty string
list = []

while n!=0:
    reminder = n%2
    list.append(reminder)
    n = n // 2
    
list.reverse()

for i in list:
    binary = binary + str(i)

print(int(binary))
print(bin(original).replace("0b", ""))

# binary to decimal

myBi = int(input("Please Enter binary Number : "))  # 101010
list = []  
decimal = 0

while myBi!=0:
    reminder = myBi % 10
    list.append(reminder)
    myBi = myBi//10
    
# 010101 

for i in range(0,len(list)):              # list[0] 1 2 3
    
    decimal = decimal + list[i]*(2**i)    # 0*(10**0) = 0+0 + 1 * 10^2 = 100

print(f"Decimal Value is : {decimal}")    
    
    

    