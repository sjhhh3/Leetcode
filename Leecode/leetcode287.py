def findDuplicate(nums):
    # Find the intersection point of the two runners.
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            # break
            return nums[tortoise]
    # Find the "entrance" to the cycle.
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1


print(findDuplicate([4,2,1,4,5,3]))