# heart pattern

print()

for x in range(3,6):
    
    # upper

    for z in range(x,5):   # space 4 3 2 1 0
        print(" ",end="")
    
    for y in range(1,2*x):  # star 1 3 5 7 9
        print("*",end="")
        
    for a in range(1,(11-2*x)):  # space 7 5 3 1
        print(" ",end="")
    
    for b in range(1,2*x):   # star 1 3 5 7 9
        print("*",end="")    
    
    print()

# lower

for x in range(1,9):
    
    for z in range(1,x+1):
       print(" ",end="")    
    
    for y in range(1,(18-2*x)+1):  # 18..1 (1,16) , (1,14) , (1,12), (1,10)  # star # 16 .. 1
        if(x==4 and y==3):
            print("S",end="")
        elif(x==4 and y==4):
            print("h",end="")
        elif(x==4 and y==5):
            print("r",end="")
        elif(x==4 and y==6):
            print("e",end="")
        elif(x==4 and y==7):
            print("y",end="")   
        elif(x==4 and y==8):
            print("a",end="")                
        else: 
            print("*",end="")
       
    print()    
    
   
 
    
#      *       *
#     ***     ***
#    *****   *****
#   ******* *******
#  *****************

print()
