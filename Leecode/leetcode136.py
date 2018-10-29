from functools import reduce
import operator
nums = [1, 2, 2, 3, 3]


print(2*sum(set(nums))-sum(nums))


print(reduce(lambda x, y: x ^ y, nums))


print(reduce(operator.xor, nums))


res = 0
#
# for num in nums:
#     res ^= num
# print(res)



dic = {}
for num in nums:
    dic[num] = dic.get(num, 0) + 1
for key, val in dic.items():
    if val == 1:
        print(key)
