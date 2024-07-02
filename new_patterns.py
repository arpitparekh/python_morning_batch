for x in range(1,6):  # 1 2 3 4 5
    
    # space
    for z in range(x,5):  # 4 3 2 1 0
        print(" ",end="")
    

    # star
    for y in range(1,x+1): # 1 2 3 4 5
        print("* ",end="")
    
    print()
    
#1     *
#3    ***
#5   *****
#7  *******
#9 ********* 

# 1,1   2,3   3,5   4,7  5,9
# y = 2*x-1

print()

for x in range(1,5):
    
    # space  0 1 2 3 4  # 1,0  2,1  3,2  4,3  5,4
    
    for z in range(1,x):
        print("  ",end="")
    
    for y in range(1,(12-2*x)):  #(1,2) (1,4) (1,6) (1,8) (1,10)
       print("* ",end="")
    
    print() 

for x in range(1,6):
    
     # space
    for z in range(x,5):  # 4 3 2 1 0
        print("  ",end="")
    
    for y in range(1,(2*x)):  #(1,2) (1,4) (1,6) (1,8) (1,10)
       print("* ",end="")
    
    print()     
      
#9     *********    # ulta pyramid
#7      *******
#5       *****
#3        ***
#1         * 

# 1,9  2,7  3,5  4,3  5,1

# 1/9  2/7 3/5 4/3 5/1 = 1/?    

# y = 11-2x


    
            