class A:
    def print(self):
        print("A")
class B:
    def print(self):
        print("B")


def function(obj):    # pass class objects into function
    obj.print()
    
a = A()
b = B()

function(a)    # name is same but behavious is different
function(b)              