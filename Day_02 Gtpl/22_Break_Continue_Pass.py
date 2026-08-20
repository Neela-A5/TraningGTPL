avlb = 10

x = int(input("How Many Candies you wnat: "))
i = 1
while i <= x:
    if x > avlb:
        print("Out of stock")
        break                 # come out of while loop
    print("Candy")
    i +=1
print("ByeeS")



for i in range(1, 30):
    if i % 3 == 0 or i % 5 == 0:
        continue                    # skip the current iteration and move to the next iteration.   
    print(i)


# Print Even number
for i in range(1, 20):
    if i % 2 != 0:
        pass
    else:
        print(i)

