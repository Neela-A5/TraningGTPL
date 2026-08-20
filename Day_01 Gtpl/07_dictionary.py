data = {1:'Navin', 2:'Harsh', 3: 'Sushma', 4:'Chandu'}
print(data[1])
print(data[3])
print(data.get(2))
print(data.get(5,'Not Found'))


keys = ['Navin', 'Chetan', 'Chandan']
values = ['Python','Java', 'JS']


data = dict(zip(keys, values))
print(data)

print(data['Navin'])
data['Monika'] = 'CS'
print(data)

del data['Chandan']
prog = {'JS':'Atom', 'CS':'VS', 'Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans', 'JEE': 'Eclipse'}}

print(prog['JS'])
print(prog['Python'])
print(prog['Python'][1])
print(prog['Java'])
print(prog['Java']['JEE'])