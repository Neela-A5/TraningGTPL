from array import *



vals = array('i', [5,3,4,-3,5,6])
print(vals)                     #array('i', [5, 3, 4, -3, 5, 6])

print(vals.buffer_info())       #(1550084313488, 6)  (address, length)

print(vals.typecode)            # i

vals.reverse()
print(vals)                      # array('i', [6, 5, -3, 4, 3, 5])

print("New Array")
newArr = array(vals.typecode, (a for a in vals))
for i in newArr:
    print(i)


val = array('I', [5,3,4,5,6])
print(val.typecode)              #I


# char Values
vals = array('u',['a','e','i','o'])
for i in vals:
    print(i)            #array('u',['a','e','i','o'])
