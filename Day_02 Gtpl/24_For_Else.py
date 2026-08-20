nums = [23,53,24, 6]
#without For_Else 
for i in nums:
    if i % 5 == 0:
        print(i)
        break
    else:
        print("Not Found")  
"""Not Found
Not Found
Not Found
Not Found
Not Found"""


# with for Else
for i in nums:
    if i % 5 == 0:
        print(i)
        break
else:
    print("Not Found")           #Not Found





num = [23,50,24,85,14,20, 5]
for i in num:
    if i % 5 == 0:
        print(i)
else:
    print("Not Found")

"""
50
85
20
5"""