def function1(a):
    print(f"function 1 => {a}")

def function2(b):
    function1(b*10)
    
function2(12)  