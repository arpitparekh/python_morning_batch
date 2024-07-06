num = int(input("Please Enter Number : "))  # 2345 - 2000
original = num

last_digit = num%10  # 5

new_last_digit = 0

count = 0

while num!=0:
    count+=1
    new_last_digit = num%10  # 5  # 4 # 3  # 2
    num = num//10   # 234 # 23  # 2 # 0
    
print(f"First Digit is : {new_last_digit}")
print(f"Last Digit is : {last_digit}") 

original = original-last_digit   # 2340

original = original - new_last_digit*(10**(count-1)) # 340

original = original + new_last_digit # 342

original = original +  last_digit*(10**(count-1))

print(f"Swapped digit number is {original}")

# 4356
# 4 , 6
# 4356 - 6 + 4 = 4354
# 4 * 1000 = 4000
# 4356 - 4000 = 354
# 6 * 1000 = 6000
# 6000 + 354 = 6354
    

