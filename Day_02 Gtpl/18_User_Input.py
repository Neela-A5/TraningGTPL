import sys
#Taking input while running code
a = int(sys.argv[1])  # 2
b = int(sys.argv[2])  # 3
z = a + b    
print(z)  #5

#Taking input after Running code
x = input("Enter !st Number: ")
y = input("Enter 2nd Number: ")
n = x + y
print(n)     # 32 

a = int(x)
b = int(y)
n = a+b
print(n)      # 5
print()


# easy method in python 
print("in Python we can dairectly convert")
x = int(input("Enter !st Number: "))
y = int(input("Enter 2nd Number: "))
print(x+y)     # 5


# Taking user input in a character formate
ch = input("Enter a char: ")  #Neela
print(ch[0])  #N


#Eval Funcation (Expressions)
result = eval(input("Enter expr: "))
print(result)
