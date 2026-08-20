a = 10   # Global variable
print(a, id(a))

def something():
    x = globals()['a']    # accessing the value of global a inside a function
    print(x, id(x))       # address of the x willl be same as address of the a

    globals()['a'] = 15    # to chaingin global variable value
    print(a)

    global z     # To convert Local Variable into Global Variable
    z = 9


something()
print(z) 