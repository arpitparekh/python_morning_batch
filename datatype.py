# datatypes

a = "bascom"

print(type(a))

a = 23

print(type(a))

a = 12.234

print(type(a))

a = 12+2j
b = 13+4j

print(a+b)
print(type(a))

# list datatype

values = [12,"Hello",12.34]

print(values)
print(type(values))

print(values[2])

values[2] = 99.99

print(values)

values.append("arpit")

print(values)

values.insert(2,4.4)

print(values)

print(values[1:3])

values.remove('arpit')

print(values)

values.remove(values[3])

print(values)

del values[2]

print(values)

data = [12,14,"Hello",'a',45.45]

new_data = data[1:3] # part range reassign

print(new_data)
print(type(new_data))

f = data[4]

print(type(f))

list1 = [1,2,3,4,5]
list2 = [9,8,7,6]

list3 = list1+list2

print(list3)

# this line i add

