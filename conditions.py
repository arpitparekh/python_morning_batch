# operators
# symbols
# < > <= >= != ==

# a = b 

a = 16
b = 13

# if else

c = a<b
print(c)
print(type(c))

if a<b:
    print("a is less than b")
else:
    print("a is greater than b")
    
x = 11
y = 13

if x<y :
    print( str(x) + " is less than "+ str(y) )
else:
    print( str(x) + " is greater than "+ str(y) )
    
# if elif else

x = 14
y = 15

if x<y:
    print("x is less than y")
elif x==y:
    print("x is equal to y")    
else:
    print("x is greater than y")

# nested if

a = 12
b = 99
c = 100

# find max from 3 numbers using if elif else

if a>b:
    if a>c:
        print('a is max')
    else:
        print('c is max')
        
else:     # a<b
    if a<b:
        print('b is max')
    else:
        print('a is max')