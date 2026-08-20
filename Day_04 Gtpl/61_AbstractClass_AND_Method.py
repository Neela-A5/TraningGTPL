#A class that provides a common structure for child classes.
# ABC Class has atleast one abc method
#An abstract method is a method that is declared in the parent class but must be implemented by its child classes.
from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
    
class Laptop(Computer):
    def process(self):
        print("its running")


class Programming:
    def work(self, com):
        print("Solving Bugs")
        com.process()

com1 = Laptop()
com1.process()

prg = Programming()
prg.work(com1)














"""class Computer:
    def process(self):
        pass

com = Computer()
com.process()
"""
