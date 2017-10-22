mynums = [10, 5, 2, 6]
myk = 100
def numSubarrayProductLessThanK(nums, k):
    counter = 0
    total = 1
    for n in range(1,len(nums)+1):
        i = 0
        while i <= len(nums)-n:
            for num in nums[i:i+n]:
                total *= num
            if total < k:
                counter += 1
            i += 1
            total = 1
    return counter

print(numSubarrayProductLessThanK(mynums, myk))