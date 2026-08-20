def search(list, n):
    i = 0
    while i  < len(list):
        if list[i] == n:
            print(n)
            print("position: ", i)
            return True
        i = i + 1
    return False
    
    


list = [1,4,2,5,6,8]
n = 3
if search(list, n): 
    print("Found: ")
else:
    print("Not Found: ")