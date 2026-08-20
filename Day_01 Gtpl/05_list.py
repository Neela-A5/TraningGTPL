nums = [25, 12,75, 95,14]
print(nums)
print(nums[0])
print(nums[4])
print(nums[2:])
print(nums[-3])

names= ['navin', 'kiran', 'john','apoorva', 'chandra']
print(names)

values = [9.5, 'Navin', 25]

mil = [nums,names]
print(mil)

nums.append(45)
print(nums)

nums.insert(2,34)
print(nums)

nums.remove(14)
print(nums)

nums.pop()
print(nums)
del nums[2:]
print(nums)

nums.extend([26,37,63,82,23])
print(nums)
min(nums)
max(nums)
sum(nums)
nums.sort()
print(nums)
