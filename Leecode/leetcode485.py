
nums = [1,1,0,1]


print("".join([str(i) for i in nums]).split('0'))

lis = ['11', '1', '111']

print(max([len(i) for i in "".join([str(i) for i in nums]).split('0')]))

print(bytearray(nums))