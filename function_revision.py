# function is a block of code that runs when we call it

def display():
    print("Hello World")
    
display()    
display()   
display()   
display()   
display()   
display()

def sum(a,b):
    print(a+b)

sum(10,20)    
sum(20,40)    
sum(50,30)    
sum(10,10) 


def mul(a,b):
    return a*b

result  = mul(10,20) + mul(20,40)  

print(result)


def myData(a):
    return a+10

print(myData(12)*10)

##############################################################

def sum1(a,b):
    return a+b

def sub(a,b):
    return a-b

print( sub( sum1(10,20) , sum1(20,30) ) )

###############################################################

## 12 + 3!

def factorial(n):
    fac = 1
    for x in range(1,n+1):
        fac = fac * x
    
    return fac

n = 12 + factorial(5)
print(n) 

##############################################################

# 1.100

for x in range(1,101):
    print(x,end="")
    
#############################################################

# function
# loop
# condition

# prime
# factorial
# palindrome    #  1234321

# 2 3 5  21 => 2..20   55 => 2..54

def prime(n):
    
    flag = True
    
    for x in range(2,n):
        if n%x == 0:
            flag = False
            break
    
    return flag  

print()
print(prime(88))          

def facto():
    pass

def pali(n):
    pass

num = 13

# 2..12

for x in range(2,12):
    # x  2 3 4 5
    if num%x==0:
        print("not prime")
    else:
        print("prime")


    