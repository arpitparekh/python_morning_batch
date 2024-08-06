# set
# frozenset

# list = [12,24,23,23]
# tuple = (12,124,423)
# dictionary = {"name":"bascom"}
# set

list = {12,243,56,34,23,35,12,35}
# can not take duplicate values
# don't no maintain order  # unordered

print(list)
print(type(list))

list.add(13)

print(list)

list2 = {55,66,77,88}
list.update(list2)

print(list)

list3 = [12,35,65]

list.update(list3)

print(list)

list.discard(12)
print(list)

list.pop()
print(list)

list.pop()
print(list)

# list => set

name = ["hello","Hi","Kem cho","hello"]

print(name)

name2 =  frozenset(name)

print(name2)



