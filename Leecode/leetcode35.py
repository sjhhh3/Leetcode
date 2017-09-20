def searchInsert(nums,target):
    # ans = 0
    # for num in nums:
    #     if num < target:
    #         ans += 1
    #         continue
    #     else:
    #         return ans
    # return ans

    x = []
    for num in nums:
        if num < target:
            x.append(num)
    return len(x)
#return len([x for x in nums if x<target])
print(searchInsert([1,3,5,6],5))