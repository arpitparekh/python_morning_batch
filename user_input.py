# take input from user

a = int(input("Enter One Number => "))
print(a)
print(type(a))

b = 18
c = 2

a = b % c    # % modulo : give the reminder  11/13
print(a)

# take year from user and check if the year is leap yeat or not

print('year is leap') if (int(input('please enter one year : ')))%4==0 else print('year is not leap')
   
# take number from user and check if the number is even of odd

# take celcius from user and convert it into ferenheight  (not if else) (-40)

# g = (9/5)*cal + 32

print("Ferenheight is =>",str((9/5)*(float(input("Insert Celcius from user : ")))+32))

# Write a program to check whether a number is divisible by 5 and 11 or not.

number = int(input('enter number : '))

if number%5==0 and number%11==0:
    print('number is divisible by 5 and 11')
else:
    print('number is not divisible by 5 and 11')
    
# check whether the number is even or odd

num = int(input("Please enter number : "))  # 34

if num%2==0:
    print("even number")
else:
    print("Odd number")
    
# check where the number is between 0..100

num = int(input("Enter Number to check in range :"))

# if 0<=num<=100:
# if 0<=num and num <=100:
if num in range(0,100):
    print("InRange")
else:
    print("OutRange")
    
    
    