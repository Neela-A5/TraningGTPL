def person(name, **data):
    print(name)
    print(data)
    print()
    print(name)
    for i,j in data.items():
        print(i,j)
person('navin', age = 26, city= 'mumbai', PhNo = 98765432)
