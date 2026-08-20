pos = -1
def search(list, n ):
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l+u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    #return False



list =[3,7, 8,9,35,67,89]
n = 67
if search(list, n):
    print("Found at Position: ", pos)
else :
    print("Not Found")