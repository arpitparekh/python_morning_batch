# find no of digit in number  1234  12//5 (integer division)

# 1234 / 10 = 123
# 123  / 10 = 12
# 12   / 10 = 1
# 1    / 10 = 0

# 645353 / 10 = 64535
# 64535  / 10 = 6453
# 6453   / 10 = 645
# 645    / 10 = 64
# 64     / 10 = 6
# 6      / 10 = 0

myNum  = int(input("Please Enter Number : "))
duplicate = myNum

count = 0

while myNum!=0:               
    myNum = myNum//10         
    count+=1       

print(f"No of Digit in {duplicate} is {count}")

# find the reverse of number and palindrome

myNum2  = int(input("Please Enter Number : "))  # 4765
duplicate = myNum2

# 1234 // 10 = 123
# 1234 % 10  = 4

rev = 0

while myNum2!=0:                    # 1234  # 123   12  1 
    last_digit = myNum2 % 10        # 4     #  3    2   1
    
    rev = rev*10 + last_digit       # 4   #  43   # 432  # 4321
    
    myNum2 //= 10                   #  123  12    1    0
    

print(f"revese of number is {rev}")

# palindrome or not

print(f"{duplicate} is {'palimdrome' if duplicate==rev else 'not plindrome'}")
    
    






