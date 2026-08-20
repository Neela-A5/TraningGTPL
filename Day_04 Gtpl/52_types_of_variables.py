# Class(Static) Variable:---> Declared inside a function.
#                     Can only be accessed within that function.

# Global Variable :---> Declared outside all functions.
#                       Can be accessed throughout the program.


class Car:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = 'BMW'

c1 = Car()
c2 = Car()

c1.mil = 8    #it will chainge the value of Local variable mil 10 to 8
           #   it will belongs to perticular object
Car.wheels = 5  #it will chainge the value of Class variable wheels 4 to 5

print(c1.com, c1.mil, c1.mil)
print(c2.com, c2.mil, c2.mil)


