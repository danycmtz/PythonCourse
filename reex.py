import re
fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'regex_sum_745121.txt'
fh = open(fname)
list = []

for line in fh:
    print(line)
    nums = re.findall('[0-9]+',line)
    print(nums)
    for num in nums:
        num = int(num)
        list.append(num)

print('There are',len(list),'values and the sum is',sum(list))
