def makeToran(size,length):
    
    for x in range(1,size):
        for y in range(1,x):
            print(" ",end="")
        
        for h in range(1,length+1):
            for z in range(1,(size*2)-2*x):
                print("*",end="")
            for y in range(2,2*x):
                print(" ",end="")  
        print()    
        
makeToran(10,8)       