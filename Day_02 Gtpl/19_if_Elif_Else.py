if True:
    print("Hello")   #Hello

if False:
    print("Hey")
print("Byee")   #Byee


x = 8
r = x % 2
if r == 0:
    print("Even")  # Even
else:
    print("Odd")


x = 7
r = x % 2
if r == 0:
    print("Even")
else:
    print("Odd")    # Odd
print("Hello Coders")



# Nested If
x = 8
r = x % 2
if r == 0:
    print("Even")  # Even
    if x > 5:
        print("Greater")     # Greater
    else:
        print("Not so greater")
else:
    print("Odd")



# If Elif Else

n = 2
if n == 1:
    print("One")
elif n == 2:
    print("Two")              #  2
elif n == 3:
    print("Three")
elif n == 4:
    print("Four")
elif n == 5:
    print("Five")
else:
    print("Number not found")