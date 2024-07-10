#      *
#     * *
#    *   * 
#   *     *
#  *********

for x in range(1,6):
    
    #space
    for z in range(x,6):  
        print(" ",end="")
    #star
    for y in range(1,(2*x)):  #(1,2)1 (1,4)3 (1,6) 5
        if(x==1 or x==5 or y==1 or y==(2*x-1)):
            print("*",end="")
        else:
            print(" ",end="")
    print()