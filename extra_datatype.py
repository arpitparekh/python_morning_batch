# numbers // string // boolean
# list

# list => group of datatype under single datatype name

data = [12,34,567,45,34,23,56,67,67]

print(data)
print(type(data))

values = [121212,12.34,"Bascom",'Jimit',True]

# we can access list values using index

print(values)
print(type(values))

print(values[4])

values[2] = "Maru Bascom"

print(values)

##################  add value in list  ##################

my_data = []    # empty list

print(my_data)

my_data.append(12)
my_data.append(12.34)
my_data.append("Jimit practice kar")

print(my_data)

values.append("Jimit Practice kar time pass nai kar")

print(values)

# values.clear()    # empty the list

# print(values)
 
print(len(values))   # find the size of the list

values.reverse()

print(values)

numbers = [12,5,567,34,23,56,86,64,34,24,23]

print(numbers)

numbers.sort()
numbers.reverse()

print(numbers)

numbers.remove(34)

print(numbers)