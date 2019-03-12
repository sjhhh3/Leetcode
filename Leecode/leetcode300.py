nums = [10,9,2,5,3,7,101,18]
def lengthOfLIS(nums):
    # def search(arr, target):
    #     L, R = 0, len(arr)
    #     while L < R:
    #         mid = L + (R - L - 1) // 2
    #         if arr[mid] < target:
    #             L = mid + 1
    #         else:
    #             R = mid
    #     return L

    import bisect

    res = []
    for n in nums:
        l = bisect.bisect_left(res, n)
        if l >= len(res):
            res.append(n)
        else:
            res[l] = n
    return len(res)

print(lengthOfLIS(nums))