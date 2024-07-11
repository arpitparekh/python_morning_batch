def plusPattern(size):
    
    if size%2==0:
        for x in range(1,size):
            for y in range(1,size):
                
                if x==(size//2) or y==(size//2):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
        
    else:
        
        for x in range(1,size+1):
            for y in range(1,size+1):
                if x==((size+1)//2) or y==((size+1)//2):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
        
    
plusPattern(17)            