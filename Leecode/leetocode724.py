
nums = [0,0,0,0,0]

def pivotIndex(nums):
    left, rsum = 0, sum(nums)
    for loc in range(len(nums)):
        rsum -= nums[loc]
        if left == rsum:
            return loc
        left += nums[loc]
    return -1
print(pivotIndex(nums))
