num = int(input("Please Enter Number : "))  # 2345

last_digit = num%10  # 5

new_last_digit = 0

while num!=0:
    new_last_digit = num%10  # 5  # 4 # 3  # 2
    num = num//10   # 234 # 23  # 2 # 0
    

print(f"First Digit is : {new_last_digit}")
print(f"Last Digit is : {last_digit}")    

