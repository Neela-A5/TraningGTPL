from functools import reduce
#Filter With Function
def is_even(n):
    return n % 2 == 0
nums = [1,2,3,4,5,6,7,8,9,3,5,2]
even = list(filter(is_even, nums))
print("Filter with Function ",even)


 
#Filter With Lambda
nums = [1,2,3,4,5,2]
even = list(filter(lambda n: n % 2 == 0, nums))
print("Filter With lambda: ",even)


#Map with Function
def add(n):
    return n+2
double = list(map(add, nums))
print("Map with Function ",double)

#Map with Lambda
double = list(map(lambda a: a + a, nums))
print("Map with Lambda", double)

#"Reduce with Function
def add_all(a, b):
    return a + b
sum = reduce(add_all,double)
print("Reduce with Function ",sum)


#Reduce with Lambda     Reduce alwase take 2 parameters
sum = reduce(lambda a,b: a+b,double)
print("Reduce with Lambda ", sum)
