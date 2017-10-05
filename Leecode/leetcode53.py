a = []


def maxSubArray(nums):
    if not nums:
        return None
    max = -(2**32)
    for i in range(0,len(nums)):
        sum = 0
        for n in range(i, len(nums)):
            sum += nums[n]
            if max < sum:
                max = sum
    return max

print(maxSubArray(a))

