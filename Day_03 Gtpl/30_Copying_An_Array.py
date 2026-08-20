from numpy import *

print("Before adding values into Array")
arr = array([1,2,3,4,5])
print(arr)
print("After adding values into Array")
arr = arr+5
print(arr)

#Adding 2 Arrays   OR   Vectorized Operations
print("Adding 2 arrays")
arr1 = array([1,3,5,7])
arr2 = array([2,4,6,8])
arr3 = arr1 + arr2
print(arr3)



#Basic Operations on Array
print(sin(arr1))
print(cos(arr1))
print(tan(arr1))
print(log(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))
print(sqrt(arr1))


#Concatinate method to combain 2 array into single array
print(concatenate([arr1,arr2]))


# Copy an array
ary = array([2,4,6,8,12])

ary1 = ary       # Both arrays are pointing to same address
print(ary, id(ary))
print(ary1, id(ary1))



print()                   #shallow Copy
arr2 = ary.view()        # Both arrays are pointing to same address
print(ary, id(ary))
print(arr2, id(arr2))




print()                    #deep Copy
arr2 = ary.copy()        # Both arrays are pointing to same address
print(ary, id(ary))
print(arr2, id(arr2))