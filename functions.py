# functions
# function is a block of code that runs when we call it
# function can be called multiple time
# reduce the boilerplate code

def python_batch():
    print("This is Coming from function")   # definition of function
    
    
python_batch()  # function calling

def my_sum(a,b):
    print(a+b)

my_sum(12,13)
my_sum(14,15)
my_sum(16,10)
my_sum(11,12)
my_sum(9,9)

def star_pattern(a):
    for x in range(1,a+1):
        print(x,end="")
    print()

star_pattern(10)
star_pattern(5)
star_pattern(100)
star_pattern(6)

def decimal_binary(number):
    print(bin(number).replace("0b", ""))
    
decimal_binary(10) 
decimal_binary(12)
decimal_binary(13)
decimal_binary(100)

def display(*data,b):     # arbitrary arguments
    print(data[b])
    

display(21,13,14,15,16,17,"kalgi","bascom",b = 6)

def my_print(name,age):                              # keyword argument
    print(f"name is {name} and age is {age}")

my_print(age=23,name="ekta")
my_print(age=25,name="kalgi")
my_print(age=27,name="krishna")

# arbitrary arguments  # **kwargs

def mera_function(**data):
    print(data["first_name"])
    
mera_function(first_name = "arpit",last_name = "parekh")


# default argument

def another_function(a=10):
    print(a)

another_function(20)

# example joie

def check_prime(num):  # 13  # 2..12   # 13/2  13/3  13/4  ... 13/12
    
    # num = 13
    
    flag = True
    
    for x in range(2,num):
        if(num%x==0):
            flag = False
            break
    
    if(flag):
        print("Prime Number che")
    else:
        print("prime number nathi")
    flag = True
    
    for x in range(2,num):
        if(num%x==0):
            flag = False
            break
    
    if(flag):
        print("Prime Number che")
    else:
        print("prime number nathi")
        

check_prime(13)
check_prime(12)
check_prime(77)
check_prime(int(input("Enter Number : ")))  # we can also give input in function para when calling