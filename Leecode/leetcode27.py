nums = [3,-3,-2,0,1,1,0,1,3]

def removeElement(nums,val):
    if not nums:
        return None
    count = 0
    lenth = len(nums)
    for n in range(0,len(nums)):
        if nums[n] != val:
            nums[count] = nums[n] #如果一样了就跳过了count的计数，从而把一个不重复的拉过来
            count += 1
        else:
            lenth -= 1
    return lenth

print(removeElement(nums,1))

'''
def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    begin = 0
    for i in range(len(nums)):
        if nums[i] == val:
            continue
        nums[begin] = nums[i]
        begin += 1
    return begin
    
    
        
i = 0

if not nums: return 0

while i < len(nums):
    if nums[i] == val:
        del nums[i]
    else:
        i += 1

return len(nums)
'''