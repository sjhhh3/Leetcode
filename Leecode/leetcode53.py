a = [-2,1,-3,4,-1,2,1,-5,4]


def maxSubArray(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    sumlist = [nums[0]]
    for i in range(1, len(nums)):
        sumlist.append(max(nums[i], sumlist[i - 1] + nums[i]))
    return max(sumlist)

print(maxSubArray(a))

