#     *
#    **
#   ***
#  ****
# *****

# *
# **
# ***
# ****
# *****

# avu j undhu

for x in range(ord("a"),ord("z")+1):
    print(chr(x))

print("#################### Pattern 1 #########################")

for x in range(1,6):  # 1 2 3 4 5             # pattern 1

    for z in range(1,x+1):
        print("* ",end="")
        
    print()

print("#################### Pattern 2 #########################")

for x in range(1,6):  # 1 2 3 4 5              # pattern 2

    for z in range(x,5):  # 1 2 3 4 (4)  # 2 3 4 (3)
        print("  ",end="")

    for y in range(1,x+1): # 1 (1)  # 2 (2)
        print("* ",end="")

    print()

# ***
# **
# *
# **
# *

print("#################### Pattern 3 #########################")

for x in range(1,6):  # 1 2 3 4 5                # pattern 3

    for z in range(x,6):
        print("* ",end="")

    print()

print("#################### Pattern 4 #########################")

for x in range(1,6):  # 1 2 3 4 5                    # pattern 4

    for y in range(1,x):
        print("  ",end="")

    for z in range(x,6):
        print("* ",end="")

    print()