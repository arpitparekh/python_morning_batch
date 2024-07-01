print()

for x in range(1,6):             # x = 1 2 3
    for y in range(1,6):         # 1 => 1 2 3 4 5  # 2 => 1 2 3 4 5  # 3 => 1 2 3 4 5
        print("* ",end="")
    print()
    
print()    
    
# 2 dimensional loop give us matrix

for x in range(1,6): # 1 2 3
    for y in range(1,x+1): # (1,2) (1,3) (1,4) (1,5) (1,6)
        print("* ",end="")
    print()
    
print()    
    
for x in range(1,6):            
    for y in range(1,6):         
        if (x==1 or x==5 or y==1 or y==5):
            print("* ",end="")
        else:
            print("  ",end="")
            
    print()    
    
print()

for x in range(1,6):             
    for y in range(1,6):         
        if (x==y or x+y==6):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
    
print()     

# 1,5  2,4  3,3  4,2  5,1  =  6