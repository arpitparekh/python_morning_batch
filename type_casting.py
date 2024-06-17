x = 10
y = 20

print(x)
print(type(x))

z = str(x)

print(z)
print(type(z))

g = 45.56
print(type(str(g)))

j = False
print(str(j))

a = 12
print(a)

print('g ni value '+str(g)+' che ane a ni value '+str(a))

# string concatination

m = 10
n = 20.34

o = m + n
print(o)
print(type(o))   # implicit casting

# int < float

a = 12
b = '12'
# print(a+b)  # error

a = 56
b = float(a)
print(b)
print(type(b))

a = False
b = str(a)
print(b)

g = 45.67
h = int(g)
print(h)
print(type(h))  # explisting casting

a = '15454'
b = int(a)
print(b)
print(type(b))

a = '12.34'
b = float(a)
print(b)
print(type(b))