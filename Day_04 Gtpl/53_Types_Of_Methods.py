#if you are working with instance then we are using self
#if you are working with class then we are using cls with decorator (@)

class Student:
    school = 'LVBV'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2= m2
        self.m3 = m3


    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3

    def get_m1(self):     #To get value with getters (Accessor)
        return self.m1
    def set_m1(self,value):    #To set value with setters (Mutator)
        self.m1 = value  

#@classmethod is a decorator in Python used to create a method that belongs to the class itself, 
#rather than to a specific object.
    @classmethod                 #
    def getschool(cls):
        return cls.school


#@staticmethod is a decorator used to define a method that belongs to a class,
# but does not need access to the object (self) or class (cls).
    @staticmethod
    def info():
        print("Static Method Body")


s1 = Student(23,64,25)
s2 = Student(63,51,16)
print(s1.avg())
print(s2.avg())
print(Student.getschool())

Student.info()

#To get value        Normally
print(s1.m1)     

