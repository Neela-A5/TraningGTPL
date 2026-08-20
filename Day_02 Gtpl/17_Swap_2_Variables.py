a = 5
b = 6
print(a,b) # 5 6

# swaping variables without using 3rd variable
a = a + b
b = a - b
a = a - b 

print(a,b)  # 6 5

a = 4
b = 7
print(a,b)  # 4 7

# swaping variables without using 3rd variable (^)
a = a ^ b
b = a ^ b
a = a ^ b 
print(a,b) # 7 4

a =2
b = 3
print(a,b)  # 2 3 
#easy Swapping Method using Python 
a,b = b, a 
print(a,b)     # 3 2