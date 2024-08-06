# loop inside loop

# *****
# *****
# *****
# *****
# *****

for x in range(1,6):  # 1 # 2 # 3 $ 4 # 5
    for y in range(1,6):
        print("*",end="")
    print()
    
print()    

# *
# **
# ***
# ****
# *****

for x in range(1,6): # 1 2 3
    
    for y in range(1,x+1): # range(1,2)  # range(1,3) # range(1,4)
        print("*",end="")
    print()      

# *****
# ****
# ***
# **
# *

print()

for x in range(1,6): # 1
    
    for y in range(1,7-x): # range(1,6) # range(1,5) # range(1,4)
        print("*",end="")
        
    print()

print()    

#     *
#    **    
#   ***
#  ****
# *****


for x in range(1,6): # 1 # 2 # 3 # 4 # 5
    
    for z in range(1,6-x): # space # 4 # range(1,5) # range(1,6)
        print(" ",end="")
        pass
    
    for y in range(1,x+1): # range(1,2)  # range(1,3) # range(1,4) # 1
        print("*",end="")
        
    print()
    

# *****
#  ****
#   ***
#    **
#     *

print()

for x in range(1,6): # 1 # 2 # 3 # 4 # 5
    
    for y in range(1,x): # range(1,2)  # range(1,3) # range(1,4) # 1
        print("  ",end="")
    
    for z in range(1,7-x): # space # 4 # range(1,5) # range(1,6)
        print(" *",end="")
        pass
    print()

#
#
#
#
#
#    
#
#
#
#
#
#
#

for x in range(1,6):   # 15 24 42 51 = 6

    for y in range(1,6):
        
        if (x==y or (x+y)==6):
            print("*",end="")
        else:
            print(" ",end="")
        
    print()
    
    
    




    




           



      
        