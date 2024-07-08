# return type of function

def display(a):
    print(a)
    
# display(12)

########################################################################

def mul(a,b):
    return a*b             # function gives us value after completing

x = mul(10,20)
print(x)

print(mul(10,13))

z = 12 + mul(10,12)        # function as value

print(z)

########################################################################

def play(a,b):
    
    print(f"a is {a} and b is {b}")
    
    return a/b

print(play(12,13))

print(type(play(10,12)))
#########################################################################

def goa(x,y):
    if x<y:
        return 10.2
    else:
        print("Budget Nathi")
    
    print("Kem cho")

print(type(goa(10,12)))

##########################################################################

def multi(a,b):
    return a/b

def sumation(a,b):
    return a+b

# function inside another function parameter

result = sumation(multi(20,10),multi(30,15))    #  (20/10 + 30/15)  

print(result)

##########################################################################

def apiCall(a):
    return a*10

def checkInternet(a):            # function returning a function
    a = 45 + a
    return apiCall(a)

print(checkInternet(10))


#########################################################################

def jump(a,b): 
    return f"a is {a} b is {b}"            # function returning a string

print(jump(12,13))

########################################################################

def check(a,b):                     # function inside a condition
    if a<b:
        return True
    else:
        return False

if check(10,11):
    print("10 nano che")
else:
    print("10 moto che")   
    
#########################################################################

def jaipur():    # useless function   # function without any body
    pass


#########################################################################

def time(x,y,/):    # another useless function only for interview
    print(x)
    print(y)

# time(y = 13,x = 12)   # not possible

#########################################################################

def bascom(*,name):
    print(name)
    
bascom(name = "time pass")

#########################################################################
    
    


    

