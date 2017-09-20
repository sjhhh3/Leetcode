nums = []
def findLengthOfLCIS(nums):
    if not nums:
        return 0
    d = {}
    count = 0
    n = 0
    for n in range(0,len(nums)-1):
        if nums[n] < nums[n+1]:
            count += 1
        else:
            d[count+1]=nums[n-count:n+1]
            count = 0
    d[count+1]=nums[n+1-count:n+2]
    return max(d.keys())

print(findLengthOfLCIS(nums))

'''
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        count = 1
        cur = 1 
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += 1
            else:
                cur = 1
            if cur > count:
                count = cur
        return count
'''




