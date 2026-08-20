from numpy import *

#2 daimentional array
arr = array([
    [1,2,3,5,8,3],
    [4,5,6,9,3,6]
])
print(arr)
print(arr,dtype)        #prints data type of array
print(ndim(arr))        #Prints the daimentions of an array
print(shape(arr))       #Prints the number of rows and columns present in the array
print(size(arr))        #Prints size of the entair block


# Converting 2D array into 1D array
arr2 = arr.flatten()
print(arr2)



# Converting 1D array into MultiDaimentional array
arr3 = arr.reshape(2,2,3)
print(arr3)


#MAtrises
#we can perform mod operations in matrices
arr1 = array([
    [1,2,3],
    [4,5,6]
])
"""

We can create like this also
m =matrix('1,2,3,4:5,6,7,8')
"""
m = matrix(arr1)
print(m)
print(m.min())



#Maltiplication in matrix
m1 =matrix('1,2,3 ; 4, 5,6 ; 7,8, 9 ')
m2 =matrix('1,2,3 ; 4, 5,6 ; 7,8, 9 ')
print(m1 * m2)
print(m1 + m2)