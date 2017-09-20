nums = [1,2,4,3,5,4,7,2]
def findNumberOfLIS(nums):
    if not nums:
        return None
    nums += [2^32]
    new = []
    count = []
    cur = 0
    ans = 1
    for i in range(1,len(nums)):
        if nums[i-1] < nums[i]:
            new.append(nums[i-1])
            count.append(cur+1)
            cur = 0
        elif nums[i-1] >= nums[i]:
            cur += 1
    if nums[-1] > new[-1]:
        new.append(nums[-1])

    for nums in count:
        if nums != 1:
            ans *= nums
    return ans

print(findNumberOfLIS(nums))