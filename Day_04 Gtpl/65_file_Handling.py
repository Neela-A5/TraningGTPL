f = open(r'MyData','r')
print(f.read())
print(f.readline(4), end = "#")


print()
print()

f1 = open('abc', 'w')
f1.write("Hello Everyone")

f1 = open('abc', 'a')
f1.write("Hello  Coder ")


f = open('Day_04 Gtpl/ad.jpg','rb')
f2 = open('MyPic.jpg', 'wb')
for i in f:
    f2.write(i)

