from numpy import *

print("Using array()")
arr = array([1,2,3,4,5], float)
print(arr.dtype)
print(arr)

print("Using linspace()")
#Creates equally spaced values between two numbers.
#This creates 5 equally spaced values from 0 to 10.
arr = linspace(0,15,4)  
print(arr)


print("Using logspace()")
#creates an array of numbers that are equally spaced on a logarithmic scale.
arr = linspace(0,14,5)  
print(arr)


print("Using arange()")
#Creates an array with values in a given range.
arr = arange(1,15,3)
print(arr)


print("Using Zeros()")
#Creates an array filled with zeros.
arr = zeros(5)
print(arr)


print("Using Once()")
#Creates an array filled with ones.
arr = ones(5)
print(arr)
# IF we want it in int values
arr = ones(5, int)
print(arr)