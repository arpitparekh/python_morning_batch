# while loop and for loop
# to do a repetative task

# inital value, condition, increment / decrement

i = 1
while i<=10:    # 1
    print(i)    # 1 , 2 .. 9
    i = i+1     # 3 , 4 .. 9 , 10
    
    
# print 1 ..100 natural numbers

i = 1
while i<=100:
    print(i)
    i+=1
    
# print 1..100 even number

i = 2
while i<=100:
    print(i)
    i+=2
    
i=1
while i<=100:   # 1
    if i%2==0:
        print(i,end= ', ')   
    i+=1
    
print()

# break continue

i = 1
while i<=5:    # 1
    if(i==3):
        i=i+1
        continue
    print(i,end=" ")
    i=i+1


# print even number between 1..100
# print odd number between 1..100
# print number between 1..100 which is divisible by 5 and 11
# print n table using while taking user input

print()

n = int(input("Enter Number : "))
i = 1

# 89 * 1 = 89
# 89 * 2 = 89
# 89 * 3 = 89
# 89 * 4 = 89
# 89 * 5 = 89
# 89 * 6 = 89
# 89 * 7 = 89
# 89 * 8 = 89
# 89 * 9 = 89
# 89 * 10 = 89

while i<=10:
    print(f"{n} * {i}   = {n*i}")
    i+=1    
    
# sum of first 10 natural numbers

i = 1
sum = 0
while i<=10:
    
    sum = sum + i # 1 , 2 , 5
    
    i+=1    
print(f"sum is {sum}")






           
    
    
    
    
    
    

        
    
        
    

    
    
    

    

    
    
    
    
