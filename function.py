# function is a block of code that runs whe we calls it
# it can help in code reuse

def ronakFunction():           # function defination
    print("Hello World")
    print("Hello Ronak")
    print(10+11)
    
ronakFunction()     # function calling
ronakFunction() 
ronakFunction() 
ronakFunction() 
ronakFunction()

# function with parameter (arguments)

def sum(a,b):
    print(a+b)
    
sum(10,20)
sum(11,21)
sum(10,56)
sum(20,20)
sum(30,11)

def multiplication(a):
    print(a*a)

multiplication(12)    
multiplication(13)    
multiplication(17)    
multiplication(99)    
multiplication(100)

# function with return type

def div(a,b):
    return a/b

x = div(10,20)

print(x)

def display(fName,lName):
    print("First Name is",fName)
    print("Last Name is",lName)

# named fuction
display(lName="Bridge",fName="Bascom")   # use parameter name while calling

######################################################

# function with the use of * can take any number of parameter inside it

def display2(*a):
    print("value : =>",a[5])
    for x in a:
        print(x)
    
display2(11,21,31,41,51,45,467,544,3432423,43654,68565854,654643)


