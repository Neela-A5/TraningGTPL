def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even +=1
        else:
            odd += 1
    return even, odd

lst = [11,20,43,82,62,2,72,8,7.9]
even, odd = count(lst)
print(even,odd)
print('Even {}, Odd {}'.format(even,odd))