#Multithreading is a technique where a program can perform multiple tasks concurrently using multiple threads.

from time import sleep
from threading import *              #Thread is used to create threads.

class Hello(Thread):        #Here, Hello inherits from the Thread class.   
    def run(self):
        for i in range(50):
            print("Hello")
            sleep(1)             #sleep() pauses execution for a specified number of seconds.
class Hi(Thread):
    def run(self):
        for i in range(50):
            print("Hii")
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
t2.start()

t1.join()
t2.join()

print("Byee")