# while for loop

i = 1
while i<=10:
    print(i)
    i+=1

for i in range(1,11):
    print(i)
         
list = [12,34,567,'bascom','vastrapur']         

for i in list:
    print(i)
    
for i in 'bascom':
    print(i)
    

# check whether the number is prime or not
# avibhajya sankya
# 2 3 5 7 11 13 17...

num = int(input("enter Number to check prime or not : "))   #    13  

if num<2:
    print("not prime")
else:
    
    flag = 0
    
    for x in range(2,num):   # 2..12
        if(num % x==0 ):
            flag = 1
            break
        
    if(flag==0):
        print("prime che")
    else:
        print("Prime Nathi")
        
# find number of vowel consonant or symbol or number inside a string

#'bascom@123'

str = input("Enter String : ")

v = 0
c = 0
d = 0
s = 0
vowels=["a","e","i","o","u","A","E","I","O","U"]

for i in str:
    if(i.isalpha()):
        
        if(i in vowels):
            v = v+1
        else:
            c = c+1
            
    elif(i.isdigit()):
        d = d+1
    else:
        s = s+1
        
print(f"Vowels are :{v}\nConsonents are :{c}\nDigits are :{d}\nSymbols are :{s}")     
                
        

        
