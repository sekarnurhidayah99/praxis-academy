class MyBaseClass:
    def __init__(self,x,y):
        self.x = x
        self.y = y
class MyDerivedClass(MyBaseClass):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z =z

class A:
    def truth(self):
        return 'All numbers are even'
    
class B(A):
    pass

class C(A):
    def truth(self):
        return 'Some numbers are even'
        

class D(B,C):
    def truth(self,num):
        if num%2 == 0:
            return A.truth(self)
        else:
            return super().truth()
            
d = D()
print(d.truth(6))
print('==================')
print(d.truth(5))
