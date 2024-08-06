# loops in python

# repetative task in python

# for  # range() datatype

for x in range(5,12):
    print(x)
    
for x in range(1,101,4):
    print(x)
    
list = [1,2,5,7,5,54,"Hello",True,1212.1212]

for x in list:
    print(x)    

name = "Bascom"

for x in name:
    print(x)
     
# while loop

n = 1  # start point

while n<=10:  # condition
    print(n)
    n = n+1   # increment -- decrement  # must require 

print(n)    

# print 1 to 100

for x in range(1,101):
    print(x)

g = 1
while(g<=100):
    print(g)
    g=g+1
    
# print even number between 1..100
    
for x in range(1,101):  # 2
    if x%2!=0:
        print(x)        