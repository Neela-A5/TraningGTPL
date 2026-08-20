def update(x):
    print(x, id(x))
    print()
    x = 8
    print('x: ', x, id(x))

a = 10
print(a, id(a))
update(a)



#In list if we are updating one element then address of that element will not be chainged

def update(lst):
    print(lst, id(lst))
    print()
    lst[2] = 45
    print('lst: ', lst, id(lst))



lst = [10,20,30]
print(lst, id(lst))
update(lst)
