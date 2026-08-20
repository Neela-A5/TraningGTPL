class A:
    def __init__(self):
        print("in A Init")
      
    def feature1 (self):
        print("Feature 1 working")

    def feature2 (self):
        print("Feature 2 working")



class B():
    def __init__(self):
            print("in B Init")
            super().__init__()
    
    def feature3 (self):
        print("Feature 3 working")

    def feature4 (self):
        print("Feature 4 working")

class C(A,B):
    def __init__(self):
        print("in C Init")
        super().__init__()

    def feature5 (self):
        print("Feature 5 working")

a1 = A()
a2 = B()
c1 = C()
c1.feature1()


