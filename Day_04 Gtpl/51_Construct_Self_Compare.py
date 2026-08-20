#A constructor is a special method that is automatically called when you create an object
#Self refers to the current object.
class Computer:
    def __init__(self):
        self.name = "Navin"
        self.age = 35
    def update(self):     
        self.age = 23
    def compare(self,other):    # self = c1,   other = c2
        if self.age == other.age:
            return True
        else:
            return False




c1 = Computer()   # Object 1     Object is saved in Heap Memory Location
c2 = Computer()   # Object 2   Every Time we will allocate new Memory adrres every for new object

#To to chainge the values 
c1.name = "Nikhil"     # Method 01


c1.update()              
if c1.compare(c2):
    print("They are same")
else: 
    print("They are different")




print(c1.name)  
print(c2.name)
