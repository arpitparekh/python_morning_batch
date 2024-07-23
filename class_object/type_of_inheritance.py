class A:
    a =1

class B(A):
    pass

# single level

class C(B):
    pass

# multi level

###############################

class X:
    pass

class Y(X):
    pass

class Z(X):
    pass

# heirarchical inheritance

###############################

class P:
    def display(self):
        print("parent class 1")
    
class Q:
     def display(self):
        print("parent class 2")
    

class R(Q,P):
    pass

# multiple inheritance

r = R()
r.display()

