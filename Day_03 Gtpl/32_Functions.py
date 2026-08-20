def great():
    print("Hello")
    print("Good Morning")

def add(a,b):
    c = a + b
    print(c)

def add(x, y ) :
    z = x + y
    return z

def add_sub(x, y ) :
    z = x + y
    r = x - y
    return z,r


great()
add(5, 6)
result = add(2,4) 
print(result)

# multipal values returned
result1, result2= add_sub(2,4) 
print(result1,result2)