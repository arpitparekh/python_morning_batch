# 12324

# find the factors of the numbers

#  34
#  1 2 17 34

num = int(input("Enter One Number : "))   # 34  # 1..34

print("Factors of given numbers are : ",end='')
for i in range(1,num+1):
    if num%i==0:
        print(i,end=' ',)
        
        
        
# 153 = 1^3 + 5^3 + 3^3 = 153

num = int(input("\nEnter One Number : "))  # 1234  => 0
original = num  # 1234
another = num

count = 0

while num!=0:
    count+=1
    num = num//10
    
print(f"No of Digit is : {count}")  # 4

# 1234 / 4 

sum = 0

while original!=0:  # 1234 # 123 # 12
    
    last = original % 10   # 4 , 3 , 2 , 1
    
    sum = sum + pow(last,count) # 256 + 3^4 + 2^4
    
    original = original // 10  # 123 # 12 # 1 
    
   
if another==sum:
    print("Number is armstrong")
else:
    print("Number is not armstrong")
    
# decimal to binary conversion
    
    
    
    






    

        
    



