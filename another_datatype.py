# varitables

# Numbers
a = 12          # int
b = 23.4        # float
c = "Bascom"    # str
d = True        # boolean

print(type(c))

# hello student

numbers = [1,2,3,5,6]

print(numbers[4])
print(len(numbers))

numbers = [12,34,354,34.34,2.4,True,"Bascom",[1,2,3]]

print(numbers[7])

# list

a = [1,2,3,4]

print(a)
print(a[2])
a[2] = 5
print(a)

a.append(45)
a.append(56)
print(a)

a.insert(4,10)
print(a)

a.pop()
a.pop()
print(a)

a.remove(4)
print(a)

a.extend([9,8,7])
print(a)

a.append('bascom') # type: ignore
print(a)

list=['hello','hi','kem cho','hola','hi']

name = "bascom bridge"
  # string is immutable
name = name.capitalize()
print(name)

# a.clear()
# print()

names = []  # empty string

b = a.copy()

print(b)
print(list.count('hi'))

print(list.index('hola'))
print(list)
list.reverse()
print(list)
list.sort()
print(list)

#################################################

# tuple

address = (1,2,4,5,6,54,3,5)  # immutable
print(type(address))

print(len(address))

#################################################

# range

l = range(5,10)   # if else loop
print(l)
print(type(l))

################################################

# num = 12

# if num in range(1,12):
#     print("He")


################################################

# dictionary
# key -value

user = {
    "name":"Rohan",
    "age":23,
    "address":"Ahmedabad",
    "name":"Roshan",
    "name":"Majnu bhai",
    True:[1,2,44],
    "Marks":(12,13,14)
}

print(user)

g = ["Name","Address","age"]
k = 10

data = {}

print(data.fromkeys(g, k))  # many to one relations

print(user.get("name"))

print(user.items())

user.pop("age")

print(user)

user.popitem()

print(user)

user.setdefault("pata","Surat")

print(user)

user.update({"name":"Mota bhai"})

print(user)

print(user.values())

# swap number without using third variable

a1 = 12
b1 = 13

print(a1)
print(b1)

a1 = a1+b1  # 25
b1 = a1-b1  # 25 - 13  # 12
a1 = a1-b1  # 25 - 12  # 13