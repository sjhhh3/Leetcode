nums1 = [4,1,2]
nums2 = [1,3,4,2]
res = []

for num in nums1:
    flag = 1
    for num2 in nums2[nums2.index(num)+1:]:
        if num2 > num:
            res.append(num2)
            flag = 0
            break
    if flag:
        res.append(-1)
print(res)