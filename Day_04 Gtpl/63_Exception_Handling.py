a = 5 
b = 0
try:
    print("Start")
    print(a / b)
    #print("Stop")
except Exception as e:
    print("Hey, You cannot divide a number by zero ", e)
    #print("Stop")
finally:
    print("resourse Closed")



#ZeroDivisionError
#ValueError