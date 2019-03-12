def maxSubArrayLen(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    sum2pos = {0: 0}
    ans = None
    tsum = 0
    for i in range(len(nums)):
        tsum += nums[i]
        wanted = tsum - k
        if wanted in sum2pos:
            length = i + 1 - sum2pos[wanted]
            if ans is None or length > ans:
                ans = length
        if tsum not in sum2pos:
            sum2pos[tsum] = i + 1
    return ans or 0


print(maxSubArrayLen([1, 2, 3, 4, 5], 10))