# operators

# symbols

# arithmetic operators

# + - / * % 
# **  exponential
# //  floor division

a = 12
b = 7

print(a**b)

print(a//b)

# assignment operator
# = += -= *= /= %=  //=  **=

a %= 10   # 4565

print(a)

print(a:=4)

# membership operator

print(12 in range(13,45))

list = [1,1,4,7,54,34,7,9,75477,65,75,57,'car']

print('car' in list)

# logical operator

# and or not

a = 34
print(not a>5)

# identity operator

# is is not
a = 5
b = 5
print()
print(a is b)
print(a==b)
print(a is not b)
print(type(a) is int)
print(type(a) is not str)
print(type(a) is not float)
print(type(a) is not list)
print(type(a) is not tuple)
print(type(a) is not dict)
print(type(a) is not set)

# what else can i do in is operator
# is operator is used to check if two variables are pointing to the same object in memory
a = [1,2,3]
b = [1,2,3]
print(a is b)

print(1+5-23+67-6*56/67*45)