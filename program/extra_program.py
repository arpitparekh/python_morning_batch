def area(radius):
    return 3.14*radius*radius

print(area(20))

###############################################################

def max(a,b):
    if a>b:
        return a
    else:
        return b

print(max(123434,13999999))    

############################################################

def no_digit(num):  # 1234
    count = 0
    while num!=0:   
        num=num//10
        count = count+1
    
    return count

n = int(input("Please Enter No of digit : "))  # 2
i = 1

while True:
    print(i) # 99
    i = i+1 
    
    if no_digit(i)>n:
        break
    
############################################################

list = [1,2,4,7,7,5,3,3,6,8]

sum = 0  # 1 # 3 # 7
for x in list:
    sum = sum +x

print("Sum is => ",sum)

############################################################

weekNumbers = [1,2,3,4,5,6,7]
weekName=["m","t","w","th","f","s","su"]

num = int(input("Enter Week Number : "))

for i in weekNumbers:
    if i == num:
        print(weekName[i-1])
        
############################################################        maximunm of three numbers





    
    



