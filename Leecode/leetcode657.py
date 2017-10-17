myinput = [1,2,2,3,1,4,2]

def findShortestSubArray(nums):
    max = 0
    maxlist = []
    maxlist2 = []
    start = 0
    end = 0
    min = 50000
    lenth = 0
    i = 0
    while i < len(nums):
        if nums.count(nums[i]) >= max:
            max = nums.count(nums[i])
        maxlist += [nums[i]]
        i += 1
    for n in maxlist:
        if n not in maxlist2:
            maxlist2.append(n)

    for n in maxlist2:

        while start < len(nums):
            if nums[start] == n:
                break
            start += 1

        nums.reverse()

        while end < len(nums):
            if nums[end] == n:
                break
            end += 1

        lenth = len(nums)-end-start

        if lenth < min:
             min = lenth

    return lenth


print(findShortestSubArray(myinput))