#A special method in Python is a method with double underscores (__) at the beginning and end of its name.
#They are also commonly called dunder methods ("double underscore").
#Python calls it automatically when you create an object:
class Computer:

    def __init__(self,cpu, ram):    # Special OR Magic Method  (Dunder)
        self.cpu = cpu
        self.ram = ram        
        print("in init")

    def config(self):             # Normal Method
        print('Config is ', self.cpu, self.ram)

com1 = Computer('i5', 16)
com2 = Computer('Ryzer 3', 8)



com1.config()
com2.config()





"""class Computer:

    def __init__(self):           # Special OR Magic Method  (Dunder)
        print("in init")

    def config(self):             # Normal Method
        print('i5, 16gb, 1TB')

com1 = Computer()
com2 = Computer()



com1.config()
com2.config()"""
