'''
def remove(nums):
    if not nums:
        return None
    d = {}
    l = []
    for i, num in enumerate(nums):
        d[num] = i
    a = sorted(d.keys())
    return a

print(remove([1]))
'''
nums = [-3,-2,0,1,1,1,3]

def removeDuplicates(nums):
    if not nums:
        return None
    count = 0
    for n in range(1,len(nums)):
        if nums[n] != nums[count]:
            count += 1
            nums[count] = nums[n] #如果一样了就跳过了count的计数，从而把一个不重复的拉过来
    return count+1

print(removeDuplicates(nums))