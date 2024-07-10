#Hollow Diamond Pattern
# ********** 
# ****  **** 
# ***    *** 
# **      ** 
# *        * 

print()

for k in range(1,47):
    
    print("*",end="")
    
print()

for x in range(1,6):
    
    for y in range(x,6):
        print("*",end="")
    
    for z in range(3,2*x+1):    # (3,3)(3,5)()
        print(" ",end="")
    
    for y in range(1,12-2*x): # (1,11)
        print("*",end="") 
     
    for z in range(3,2*x+1):    # (3,3)(3,5)()
        print(" ",end="")
        
    for y in range(1,12-2*x): # (1,11)
        print("*",end="") 
    for z in range(3,2*x+1):    # (3,3)(3,5)()
        print(" ",end="")
    for y in range(1,12-2*x): # (1,11)
        print("*",end="") 
    for z in range(3,2*x+1):    # (3,3)(3,5)()
        print(" ",end="")
    for y in range(1,12-2*x): # (1,11)
        print("*",end="") 
    for z in range(3,2*x+1):    # (3,3)(3,5)()
        print(" ",end="")
    for y in range(x,6):
        print("*",end="")                                    

    print()

print()    

# for x in range(1,6):
    
#     for y in range(1,x+1):
#         print("*",end="")
    
#     for z in range(1,11-2*x):    # (11,10)(3,5)()
#         print(" ",end="")
    
#     for y in range(1,x+1):
#         print("*",end="")    

#     print()
    


# *        * 
# **      ** 
# ***    *** 
# ****  ****
# **********

# class and objects



