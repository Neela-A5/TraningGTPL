num = 2.5
print(type(num))

num = 5
print(type(num))

num = 6 + 9j
print(type(num))

a = 5.6
b = int(a)
print(type(b))

b = 5
k = float(b)
print(k)
k  = 6

c = complex(b, k)
print(c)

print(b < k)

bool = b < k
print(bool)

print(type(bool))
print(int(True))
print(int(False))

lst = [25, 36, 45, 15, 12, 25]
print(lst)
type(lst)

s = {23,53,17,63}
print(s)
type(s)

t = (27,27,97,53,93)
print(t)
print(type(t))

str = "Neela"
st = 'a'
print(type(st))


r = range(10)
print(r)

rg = list(range(10))
print(rg)

cnvt = list(range(2,10,2))
print(cnvt)
print(type(cnvt))

d = {'navin':'Samasang', 'rahul':'Moto', 'Kiran': 'OnePlus'}
print(d)
print(d.keys())
print(d.values())
print(d['navin'])
print(d.get('kiran'))
print(d.get('rahul'))