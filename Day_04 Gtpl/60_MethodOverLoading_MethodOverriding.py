"""Method Over Loading is dairectlynot supported in Pytho
nclass Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self, a = None,b = None,c = None):
        if a != None and b != None and c != None:
            return a + b + c
        elif a != None and b != None : 
            return a + b
        else:
            s =a
        return s
        


s1 = Student(23,53)
print(s1.sum(2,3,4))"""


class A:

    def show(self):
        print("in A Show")
 
class B(A):
    def sho(self):
        print("in B Show")



a1 = B()
a1.show()
