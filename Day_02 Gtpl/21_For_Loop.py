x = ['navin', 46, 3.5]
# It prints all value at Once
print(x) #  ['navin', 46, 3.5]

# print one by one values
for i in x : 
    print(i) 
"""
navin
46
3.5    """


# To print character from String
n = 'navin'
for i in n:
    print(i) 
"""
n
a
v
i
n """



for i in [4,2,'Neela','N']:
    print(i)

# prints ascendig order
for i in range(11,18,2):
    print(i)
print()


# prints descendig order
for i in range(18, 8,-2):
    print(i)

for i in range(1, 21):
    if i % 5 == 0:
        print(i)