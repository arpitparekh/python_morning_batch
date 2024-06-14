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

fruit = (23,76,'hello')
print(fruit)
print(type(fruit))


x = range(8) #used for loops
print(x)

#dictionary
#key : value

employee = {"name":"krishna",
            "email" : "krishna.123@gmail.com", 
            "address": "satellite",
            3 : "hello"}
print(employee)
print(type(employee))

name = []  #empty list // append // insert

print(employee[3])

employee[3] = "Hi"   # directory value re assign

print(employee[3])

myData = {}
myData.update({"first_name" : "parekh"})

employee.update({"age":"45"})

print(myData)
print(employee)

employee.pop("age")

print(employee)

employee.popitem()

print(employee)

del employee["address"]

print(employee)

employee.clear()  # empty the dictionary

# del employee  # delete the variable

print(employee)

# set datatype

voo = {'hello',23,45.4,'hsfsdf'} # unorder

print(voo)
print(type(voo))

voo.add("coco") # can add new item

print(voo)

voo.add('hello') # cannot add same item

print(voo)

voo.remove(23)
# voo.remove(voo[1])

print(voo)

print(len(voo))  # find the length

# frozenset function

my_list = [1,2,3,"hello",False]

my_new_list = frozenset(my_list)

print(my_new_list)
print(type(my_new_list))

# boolean datatype

isLogin = 1
print(bool(isLogin))

my_expression = 12 != 13

print(my_expression)

my_expression = 10 < 9

print(my_expression)

x = None
print(x)
print(type(x))




