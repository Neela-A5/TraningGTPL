
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(50)
print(sys.getrecursionlimit())



def great():
    print("Hello")
great()




print()
def great1():
    print("Hello")
    great1()
great1()

