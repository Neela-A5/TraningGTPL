class TopTen:


    def __init__(self):
        self.num= 1     #iterator starts from 1.

    def __iter__(self):      #This object itself can act as an iterator.
        return self
    
    def __next__(self):      #This method tells Python what the next value should be.
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration        #StopIteration → stop the loop
    
values = TopTen()
for i in values:
    print(i)