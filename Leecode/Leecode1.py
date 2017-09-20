'''
def TwoSum(nums,target):
    d={}
    for i,nums in enumerate(nums):
        if target-nums in d:
            return i
        d = nums


numbs = [3,2,4]
target = 6
d = {}
for i,num in enumerate(numbs):
    if target-num in d:
        print(target-num,d[target-num],i)
    d[num] = i
    print (d)

d = {1:'baby',5:'haha','z':'lol'}
print(d['z'])
'''
# Problem 1
class Solution(object):
    def twoSum(self,nums,target):
        d = {}
        for i, num in enumerate(nums):
         if target - num in d:
              return (d[target - num], i)
         d[num] = i

ans = Solution()
numbs = [3, 2, 4]
print(ans.twoSum(numbs, 6))