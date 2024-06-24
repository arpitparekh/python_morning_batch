# for loop

# initial value
# condition
# increment / decrement

for x in range(2,11,3):
    print(x)
    
list = [12,35,32,6,675]

# 12  find index

print(list)

for x in list:
    print(x)
    
for x in 'bascom institute':
    print(x)
    
# list = [12,35,32,6,675] add 10 in each element

# list[0] = 34

for x in list:   #  x = 12 , x = 22 , 22
    print(x)
    
for x in range(len(list)): # 0 ..4
    print(list[x])    
    
for x in range(len(list)):  # 0 , 4
    list[x] = list[x]+10  

print(list)

values = [12,5,4,7,9,7,534,2335,5643,4343,4433]

min = values[0]  # 4
for x in values:
    
    if x<min:
        min = x
        
print(f"min number in given list is {min}")        

    