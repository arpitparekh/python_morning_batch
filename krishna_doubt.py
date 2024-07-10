for x in range(3,6):
    
    #space
    for z in range(x,5):
        print(" ",end="")
    
    for y in range(1,2*x-1):
        print("*",end="")
        
    for a in range(1,(12-2*x)):
        print(" ",end="")
        
    for b in range(1,2*x-1):
        print("*",end="")
        
    print()
        
    #lower
        
        
for x in range(1,9):
        
    for z in range(1,x+1):
        print(" ",end="")
        
        
    for y in range(1,(18-2*x)):                      #1/16  1/14  1/12  1/10
        
        
        if (x==2 and y==4):
            print("J",end="")
        elif (x==2 and y==5):
            print("I",end="")
        elif (x==2 and y==6):
            print("T",end="")
        elif (x==2 and y==7):
            print("A",end="")
        elif (x==2 and y==8):
            print("R",end="") 
        elif (x==2 and y==9):
            print("T",end="") 
        elif (x==2 and y==10):
            print("H",end="")  
        else:           
            print("*",end="")
        
    print()
    
    
    
for x in range(1,6):
    
    for y in range(1,6):
        if x==1 or x==5 or y==1 or y==5 :
            print("* ",end="")
        else:
            print("  ",end="")
        
    print()
    
    
for x in range(1,8):
    for y in range(1,x+1):
        if x==7 or  y==1 or y==x:
            print("*",end="")
        else:
            print(" ",end="")
        
    print()
    
    
    
for x in range(1,6):
    for z in range(x,6):
        print(" ",end="")
        
    for y in range(1,x+1):
        if x==1 or x==5 or y==1 or y==5 or y==x:
            print("* ",end="")
            
        else:
            print("  ",end="")
        
    print()
    
print()
        
#inverted triangle

for x in range(1,6):
    for y in range(x,6):
        print("* ",end="")
        
    print() 
    
    
print()  

#12. Hollow Inverted Right Triangle Pattern

for x in range(1,6):
    for y in range(x,6):
        if x==1 or x==5 or y==1 or y==5 or y==x:
            print("*",end="")
        else:
            print(" ",end="")
            
    print()
    
print()

#Mirrored Inverted Right Triangle

for x in range(1,6):
    
    for z in range(1,x+1):
        print(" ",end="")
        
    for y in range(x,6):
        print("*",end="")
    
    print()
    
print()


for x in range(1,6):
    
    for z in range(1,x+1):
        print(" ",end="")
        
    for  y in range(x,6):
        if x==1 or x==5 or y==1 or y==5 or y==x:
            print("*",end="")
            
        else:
            print(" ",end="")
            
    print()
    
print()


# Pyramid Pattern

for x in range(1,6):
    
    for z in range(x,6):
        print(" ",end="")
    for y in range(1,2*x):           #1/1  2/3  3/5  4/7  5/9 
        print("*",end="")
        
    print()
    
print()


# pyramid and hollow
for x in range(1,6):
    
    for z in range(x,6):
        print(" ",end="")
    for y in range(1,2*x):
        if x==1 or x==5 or y==1 or y==(2*x-1):
            print("*",end="")
        else:
            print(" ",end="")
        
    print()
    
print()

# #17. Inverted Pyramid Pattern
# *********
#  *******
#   *****
#    ***
#      *


for x in range(1,6):
    
    for z in range(1,x+1):
        print(" ",end="")
    for y in range(1,12-2*x):
        print("*",end="")
        
    print()
    
print()

# 18. Inverted Hollow Pyramid Pattern
# ********* 
#  *     * 
#   *   * 
#    * *
#     *
for x in range(1,6):
    
    for z in range(1,x+1):
        print(" ",end="")
    for y in range(1,12-2*x):
        if x==1 or x==5 or y==1 or y==(11-2*x):   #1/9  2/7  3/5 4/3 5/1
           print("*",end="")
           
        else:
            print(" ",end="")
        
    print()
    
########################################################################################################
# 19. Half Diamond Pattern
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
for x in range(1,5):
    for y in range(1,x+1):
        print("*",end="")
    print()
    
for x in range(1,6):
    for y in range(x,6):
        print("*",end="")
        
    print()
##############################################################################################
   
# 20. Mirrored Half Diamond Pattern
#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *


for x in range(1,6):
    for z in range(x,6):
        print(" ",end="")
    for y in range(1,x+1):
        print("*",end="")
    print()
    
for x in range(1,5):
    for z in range(1,x+2):
        print(" ",end="")
    for y in range(x,5):
        print("*",end="")
        
    print()
 
 
 #################################################################################   
# 21. Diamond Pattern
#     *
#    ***
#   *****
#  *******
# *********
#  *******         1/1   
#   *****
#    ***
#     *
print()


for x in range(1,6):
    for z in range(x,6):
        print(" ",end="")
    for y in range(1,2*x):
        print("*",end="")
        
    print()
    
for x in range(1,5):
    for z in range(1,x+2):
        print(" ",end="")
    for y in range(1,10-2*x):
        print("*",end="")
        
    print()
    
    
print()


# 22. Hollow Diamond Pattern
# ********** 
# ****  **** 
# ***    *** 
# **      ** 
# *        * 
# *        * 
# **      ** 
# ***    *** 
# ****  ****
# **********
#upper

for x in range(1,6):
    
    for y in range(x,6):
        print("*",end="")
        
    for z in range(1,2*x-1):
        print(" ",end="")
        
    for y in range(x,6):
        print("*",end="")
       
    print()   
#lower

for x in range(1,6):
    
    for y in range(1,x+1):
        print("*",end="")
        
    for z in range(1,11-2*x):
        print(" ",end="")
        
    for y in range(1,x+1):
        print("*",end="")      
        
    print()
    
print()


# 23. Right Arrow Star Pattern
#     ***** 
#       ****
#         *** 
#           **
#             * 
#           **
#         ***
#       ****
#     *****


for x in range(1,6):
    
    for z in range(1,2*x):
        print(" ",end="")
        
    for y in range(x,6):
        print("*",end="")
        
    print()

for x in range(1,5):
    
    for z in range(1,10-2*x):
        print(" ",end="")
        
    for y in range(1,x+2):
        print("*",end="")
        
    print()   

print()

# 24. Left Arrow Pattern
#      ***** 
#     ****
#    *** 
#  **
# * 
#  **
#    *** 
#     ****
#       *****


for x in range(1,6):
    
    for z in range(1,10-2*x):
        print(" ",end="")
        
    for y in range(x,6):
        print("*",end="")
    
    print()
    
for x in range(1,5):
    
    for z in range(1,x+1):
        print(" ",end="")
        
    for y in range(1,x+2):
        print("*",end="")
        
    print()
               
print()  

             
#  25. Plus Pattern
#     +
#     +
#     +
#     +
# ++++++++++
#     +
#     + 
#     +
#     +       

for x in range(1,11):
    for y in range(1,11):
        if x==5 or y==5:
            print("*",end="")
        else:
            print(" ",end="")
    print() 
    
print()  


# 26. X Pattern
# ** ** ** **
# *
# ** ** ** **

for x in range(1,10):
    for y in range(1,10):
        if x==y or x+y==10:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
