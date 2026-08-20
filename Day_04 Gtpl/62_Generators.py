#A generator is a special type of iterator that produces values one at a time, instead of storing all values at once.
def topten():
    n =1 
    while n <= 10:
        sq = n*n
        yield sq     #generator function. #returns a value one at a time
        n += 1

values = topten()
for i in values:
    print(i)