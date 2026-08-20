#Actual & Formal PArameter
def add(a,b):    #(a,b) --> Formal Parameter
    c = a + b
    print(c)

add(5,6)          #(a,b) --> Actual Parameter


"""
  4 Types in Actual Parameters
1> Position
2> Keyword
3> Default
4> Variable Length
"""

#Position 
def person(name, age):
    print(name)
    print(age)
person('navin', 27)

#Keyword
def person(name, age):
    print(name)
    print(age+1)
person(age = 27, name = 'navin')

#Default
def person(name, age = 10):
    print(name)
    print(age)
person('navin')

#Variable Length
def sum(a,  *b):
    c = a
    for i in b:
        c = c + i
    print(c)
sum(5,3,75,6)