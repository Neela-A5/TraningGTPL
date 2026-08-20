class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    def show(self):
        print(self.name, self.rollno)   #by calling show() we can print all values that present in method
        self.lap.show()

    class Laptop:             # Inner Class
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5' 
            self.ram = 8
        def show(self):
            print("LAPTOP: ",self.brand, self.cpu,self.ram)

            

s1 = Student('Navin', 819)
s2 = Student('Neela', 423)
s1.show()


print(s1.lap.brand)   # To access brand from inner class   Way 01
# It willcreate another object of
lap1 = s1.lap
lap2 = s2.lap
print(id(lap1))
print(id(lap2))


l1 = Student.Laptop()
print(l1.show())
